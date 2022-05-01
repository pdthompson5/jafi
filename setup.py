from importlib_metadata import entry_points
from setuptools import setup
from setuptools import find_packages


setup(
    name="jafi",
    version="1.0.0",
    description="Small functional language interpreter",
    author="Phil Thompson",
    author_email="pdthompson5.@crimson.ua.edu",
    url="https://github.com/pdthompson5/jafi",
    install_requires=[],
    packages=["jafi"],
    # entry_points={
    #     'console_scripts:'[
    #         'run_jafi jafi.main:Main'
    #     ]
    # }
    



)