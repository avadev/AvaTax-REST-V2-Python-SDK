"""Set up file, to install this module : pip install -e ."""
from setuptools import setup

setup(
    name='Avalara Python SDK',
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
    install_requires=['requests', 'ipython'],
    extras_require={
        "test": ['pytest', 'pytest-cov', 'tox']
    })
