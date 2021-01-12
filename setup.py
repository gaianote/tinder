import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

VERSION = "0.0.1"

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tinder",
    version=VERSION,
    packages=["tinder"],
    url="",
    author="gaianote",
    author_email="gaianote311@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    entry_points={"console_scripts": ["tinder = tinder.app:main"]},
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
            "mypy",
            "flake8",
            "black",
            "isort",
            "pytest-cov",
            "pre-commit",
        ]
    },
)
