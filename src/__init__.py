"""Return type checking tuple based on Python version of environment."""
import sys


if sys.version_info.major == 3:
    str_type = (str, type(None))
else:
    str_type = (str, unicode, type(None))
