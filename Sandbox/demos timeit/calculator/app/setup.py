# python3.10 setup.py py2app

from setuptools import setup

setup(
    app=["calculator_with_labels.py"],
    setup_requires=["py2app"],
)