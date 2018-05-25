"""Set up file, to install this module : pip install -e ."""
from setuptools import setup

setup(
    name='Avalara',
    version='18.5.1',
    url='https://github.com/avadev/AvaTax-REST-V2-Python-SDK',
    package_dir={'': 'src'},
    py_modules=[
        'client',
        'client_methods',
        'transaction_builder',
        'transaction_builder_methods',
        '_str_version'
    ],
    author='Han Bao, Adrienne Karnoski, Robert Bronson, Philip Werner',
    author_email='han.bao@avalara.com',
    description='Avalara Tax Python SDK.',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=['requests', 'ipython'],
    extras_require={
        "test": ['pytest', 'pytest-cov', 'tox']
    })
