import codecs
import os
import re

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="bugmenot",
    version=find_version("bugmenot", "__init__.py"),
    url="http://github.com/ptrstn/bugmenot",
    author="Peter Stein",
    license="Unlicense",
    packages=["bugmenot"],
    install_requires=["requests", "beautifulsoup4"],
    entry_points={"console_scripts": ["bugmenot=bugmenot.__main__:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
