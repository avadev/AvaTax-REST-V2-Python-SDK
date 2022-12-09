import functools
import logging
import json
import time

import requests

from . import client



def ava_log(func):
    """
    Function decorator for implementation of logging
    @param func: function where logging needs to be implemented
    @return: function
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger()
        is_log_req_resp_allowed = False
        ava_log_entry = {}
        is_error_log = False

        # Logic :
        # 1) Check if decorator is called for function in AvaTaxClient class
        # 2) If logger is set then use it else use new instance of logger (this property is useful when SDK consumer
        #    wants to use specific configuration)
        # 3) Execute actual method and create log entry in case of http response only
        # 4) In case of exception though log error
        execution_start_time = time.perf_counter()
        try:
            if isinstance(args[0], client.AvataxClient):
                if hasattr(args[0], "logger") and (args[0].__getattribute__("logger") is not None):
                    logger = args[0].__getattribute__("logger")
                if hasattr(args[0], "is_log_req_resp_allowed"):
                    is_log_req_resp_allowed = args[0].__getattribute__("is_log_req_resp_allowed")
            result = func(*args, **kwargs)
            if result is not None and isinstance(result, requests.models.Response):
                ava_log_entry = get_ava_log_entry(result, is_log_req_resp_allowed)
            return result
        except Exception as e:
            is_error_log = True
            ava_log_entry["error"] = str(e)
            raise e
        finally:
            total_execution_time = time.perf_counter() - execution_start_time
            if "execution_time" not in ava_log_entry:
                ava_log_entry["execution_time"] = total_execution_time * 1000
            json_data = json.dumps(ava_log_entry, indent=4)
            if is_error_log:
                logger.error(json_data)
            else:
                logger.info(json_data)

    return wrapper


def get_ava_log_entry(result: requests.Response, is_log_req_resp_allowed: bool) -> dict:
    log_entry = {}
    log_entry["execution_time"] = result.elapsed.total_seconds() * 1000
    log_entry["x-correlation-id"] = result.headers["x-correlation-id"]
    log_entry["status_code"] = result.status_code
    log_entry["request_url"] = result.url
    log_entry["method"] = result.request.method
    if is_log_req_resp_allowed:
        log_entry["request"] = str(result.request.body)
        log_entry["response"] = result.text

    return log_entry


def decorate_all_methods(decorator, exclude=["__init__", "add_credentials"]):
    """
    Decorator to be applied at class level. This decorator decorates all methods in class with
    supplied decorator in parameter.
    @param decorator: decorator to be applied to all methods in class
    @param exclude: list of methods to exclude from being decorated.
    @return: class with decorated methods
    """

    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)) and attr not in exclude:
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls

    return decorate
