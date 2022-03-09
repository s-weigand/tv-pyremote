#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = [
    "Flask>=1.1.2",
    "flask-restx>=0.2.0",
    "PyAutoGUI>=0.9.52",
    "qrcode>=6.1 ",
    "Click>=7.1.2",
]

setup_requirements = ["pytest-runner"]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Sebastian Weigand",
    author_email="s.weigand.phy@gmail.com",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="Flask app which can be used as a remote control for \
                 your PC when watching movies/series.",
    entry_points={
        "console_scripts": [
            "tv_pyremote=tv_pyremote.cli:main",
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    project_urls={
        "Documentation": "https://tv-pyremote.readthedocs.io/en/latest/",
        "Source": "https://github.com/s-weigand/tv-pyremote",
        "Tracker": "https://github.com/s-weigand/tv-pyremote/issues",
    },
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="tv_pyremote",
    name="tv_pyremote",
    packages=find_packages(include=["tv_pyremote", "tv_pyremote.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/s-weigand/tv-pyremote",
    version="0.1.0",
    zip_safe=False,
)
