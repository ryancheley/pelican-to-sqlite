import io
import os

from setuptools import find_packages, setup

VERSION = "0.3.0"


def get_long_description():
    with io.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="pelican-to-sqlite",
    description="CLI tool for loading local pelican markdown files into a SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Ryan Cheley",
    version=VERSION,
    license="Apache License, Version 2.0",
    packages=find_packages(),
    install_requires=["sqlite-utils", "click", "html2text", "pelican"],
    extras_require={"test": ["pytest"]},
    tests_require=["pelican-to-sqlite[test]"],
    setup_requires=["pytest-runner"],
    entry_points="""
        [console_scripts]
        pelican-to-sqlite=pelican_to_sqlite.cli:cli
    """,
    url="https://github.com/ryancheley/pelican-to-sqlite",
    project_urls={
        "Issues": "https://github.com/ryancheley/pelican-to-sqlite/issues",
        "CI": "https://github.com/ryancheley/pelican-to-sqlite/actions",
        "Changelog": "https://github.com/ryancheley/pelican-to-sqlite/releases",
    },
    python_requires=">=3.7",
)
