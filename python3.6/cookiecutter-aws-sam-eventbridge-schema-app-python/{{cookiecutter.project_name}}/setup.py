from setuptools import setup, find_packages
{% set schema_package = cookiecutter.AWS_Schema_root.split('.')[0] %}
setup(
    name="{{ schema_package }}", 
    version="1.0",
    package_dir={"":"{{ cookiecutter.function_name }}"},
    packages=find_packages(where="{{ schema_package }}"),
)
