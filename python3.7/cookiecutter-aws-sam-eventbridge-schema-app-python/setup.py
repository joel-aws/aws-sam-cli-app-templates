{% set schema_root = cookiecutter.AWS_Schema_root.split('.')[0] %}
from setuptools import setup

setup(
    name="{{ schema_root }}", version="1.0", packages=["{{ cookiecutter.function_name }}/{{ schema_root }}"],
)
