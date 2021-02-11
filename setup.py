# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Lambdata_pt2", # the name that you will install via pip
    version="1.0",
    author="Cassidy Ellis ",
    author_email="cassidyhaellis@email.com",
    description=" This package is compiled with module to perform varies operations",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/cassidyhanna/Lambdata",
    #keywords="",
    packages=find_packages() # ["my_lambdata_pt2"]
)
