from setuptools import find_packages, setup

__package_name__ = "hive_metastore_client"
__version__ = "1.0.9"
__repository_url__ = "https://github.com/quintoandar/hive-metastore-client"

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name=__package_name__,
    description="A client for connecting and running DDLs on Hive Metastore with Thrift protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="hive hive-metastore hive-client hive-metastore-client metastore",
    version=__version__,
    url=__repository_url__,
    packages=find_packages(
        exclude=(
            "docs",
            "tests",
            "tests.*",
            "pipenv",
            "env",
            "examples",
            "htmlcov",
            ".pytest_cache",
        )
    ),
    license="Copyright",
    author="QuintoAndar",
    install_requires=requirements,
    extras_require={},
    python_requires=">=3.7, <4",
)
