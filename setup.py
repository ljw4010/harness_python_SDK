# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "harness_python_sdk"
VERSION = "v1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="Harness NextGen Software Delivery Platform API Reference",
    author_email="contact@harness.io",
    url="",
    keywords=["Swagger", "Harness NextGen Software Delivery Platform API Reference"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown"
)
