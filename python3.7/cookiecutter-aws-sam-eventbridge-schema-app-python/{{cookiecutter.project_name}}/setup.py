from setuptools import setup
{% set schema_package = cookiecutter.AWS_Schema_root.split('.')[0] %}
setup(
    name="{{ schema_package }}", version="1.0", packages=["{{ cookiecutter.function_name }}/{{ schema_package }}"],
)
