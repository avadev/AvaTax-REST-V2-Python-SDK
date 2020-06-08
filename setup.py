"""Set up file, to install this module : pip install -e ."""
from setuptools import setup


pkg_description = ''
with open('README.md') as f:
    pkg_description = f.read()


setup(
    name='Avalara',
    version='20.6.0',
    url='https://github.com/avadev/AvaTax-REST-V2-Python-SDK',
    package_dir={'': 'src'},
    packages=['avalara'],
    author='Han Bao, Adrienne Karnoski, Robert Bronson, Philip Werner, Genevieve Conty',
    author_email='han.bao@avalara.com',
    description='Avalara Tax Python SDK.',
    long_description=pkg_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=['requests'],
    extras_require={
        "test": ['pytest', 'pytest-cov', 'tox']
    })
