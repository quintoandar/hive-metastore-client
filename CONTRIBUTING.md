# Contributing to Hive Metastore Client

:tada: :clap:  Thank you for wanting to contribute and be part of this project! :clap: :tada:

This document describes our guidelines for contributing to Hive Metastore Client and its modules. The content will help
 you with guides so you can contribute more easily and, as a consequence, the code can maintain a high quality standard.
 Not all possible cases will be covered in this document, so we hope you use your best judgment, and feel free to help 
 us enhance this document in a pull request. 

### Table of Contents
  * [Development Environment](#development-environment)
    + [Getting started](#getting-started)
      - [1. Clone the project:](#1-clone-the-project-)
      - [2. Setup the python environment for the project:](#2-setup-the-python-environment-for-the-project-)
        * [Errors](#errors)
      - [3. Install dependencies](#3-install-dependencies)
        * [Errors](#errors-1)
      - [Project](#project)
  * [Styleguides](#styleguides)
    + [Python Styleguide](#python-styleguide)
      - [Type Hint](#type-hint)
    + [Documentation Styleguide](#documentation-styleguide)
  * [Tests](#tests)
  * [Documentation](#documentation)
  * [GitFlow](#gitflow)
  * [Pull Requests](#pull-requests)
    + [Creating a Pull Request](#creating-a-pull-request)
      - [Good branch name](#good-branch-name)
      - [Create small PRs](#create-small-PRs)
      - [Add good description](#add-good-description)
      - [Add labels](#add-labels)

## Development Environment

At the bare minimum you'll need the following for your development
environment:

1. [Python 3.7.6](http://www.python.org/)


It is strongly recommended to also install and use [pyenv](https://github.com/pyenv/pyenv):

 - [pyenv-installer](https://github.com/pyenv/pyenv-installer)

This tool eases the burden of dealing with virtualenvs and having to activate and deactivate'em by hand. Once you run 
`pyenv local my-project-venv` the directory you're in will be bound to the `my-project-venv` virtual environment and 
then you will have never to bother again activating the correct venv.

### Getting started

#### 1. Clone the project:

```bash
    git clone git@github.com:quintoandar/hive-metastore-client.git
    cd hive-metastore-client
```

#### 2. Setup the python environment for the project:

Run `make help` for more information on ready to use scripts.

```bash
make environment
```

If you need to configure your development environment in your IDE, notice
pyenv will store your python under
`~/.pyenv/versions/hive-metastore-client/bin/python`.

##### Errors

If you receive one error of missing OpenSSL to run the `pyenv install`, you can try to fix running:

```bash
sudo apt install -y libssl1.0-dev
```

#### 3. Install dependencies

```bash
make requirements-all
```

##### Requirements
The requirements of the project were split in order to better organize and facilitate the installation of both full and individual sets of requirements, according to each one's needs.
```
|-- requirements.dev.txt        < for developing / changing the source code >
|-- requirements.lint.txt       < for linting code >
|-- requirements.test.txt       < for running unit and integration tests >
|-- requirements.txt            < for the project being able to run in a production environment >
|-- docs/requirements.docs.txt  < for recreating the documentation's files >
```

##### Errors

If you receive one error like this one:
```bash
 "import setuptools, tokenize;__file__='/tmp/pip-build-98gth33d/googleapis-common-protos/setup.py';
 .... 
 failed with error code 1 in /tmp/pip-build-98gth33d/googleapis-common-protos/
```
 
You can try to fix it running:

```bash
python -m pip install --upgrade pip setuptools wheel
```

#### Project

Library's content live under the [_hive_metastore_client_](https://github.com/quintoandar/hive-metastore-client/tree/main/hive_metastore_client) module, where you'll find the client [main class](https://github.com/quintoandar/hive-metastore-client/blob/main/hive_metastore_client/hive_metastore_client.py).

## Styleguides

### Python Styleguide

TL;DR: 
- Just run `make apply-style` before you commit. 
- Check if everything is fine with `make checks`.

This project follows:
- [PEP8](https://www.python.org/dev/peps/pep-0008/) for code style.
- [PEP257](https://www.python.org/dev/peps/pep-0257/) for docstring style with 
reStructuredText format. 

This project uses some nice tooling to unify style across the project's codebase
 and improve quality. You don't need to worry about manually reviewing your 
 style and imports, `black` will automatically fix most of style inconsistencies:

```bash
make apply-style
```

Additionally [Flake 8](http://flake8.pycqa.org/en/latest/) is used to check for 
other things such as unnecessary imports and code-complexity.

You can check Flake 8 and Black by running the following within the project root:

```bash
make checks
```

#### Type Hint

We use type hint in all of our methods arguments and in the return of the methods 
too. This way, our methods will have a very explicit declaration of their expected 
inputs and outputs, making it easier for anyone to understand them. Besides, using 
type hints will help us with documentation and make it easier to find/prevent bugs.
 More information can be found in Python [docs](https://docs.python.org/3/library/typing.html)

Example:
```Python
def read(self, format: str, options: dict, stream: bool = False) -> DataFrame:
```

We use [Mypy](http://mypy-lang.org/) for static type checking.
The command `make checks` will analyse the typing. But if you desire you can run
`make type-check` for analysing only the typing.

### Documentation Styleguide

We chose the python reStructuredType format for docstrings

You can easily configure PyCharm to use this style in "Python Integrated Tools":

![](https://user-images.githubusercontent.com/13151948/100780284-48199f00-33e8-11eb-9099-cdf44aca7266.png)


There is **no need to write about the types** of arguments or returns of a method since we decide to use type hints instead. By using [this](https://pypi.org/project/sphinx-autodoc-typehints/) plugin, metadata about types in documentation can be easily generated by Sphinx.

Example of class documentation:
```Python
class ColumnBuilder(AbstractBuilder):
    """Builds thrift FieldSchema object."""

    def __init__(self, name: str, type: str, comment: str = None) -> None:
        """
        Constructor.

        :param name: name of the field
        :param type: type of the field
        :param comment: column's comment
        """
        self.name = name
        self.type = type
        self.comment = comment
```

## Tests

TL;DR: Just run `make tests` to check if your code is fine.

This project is thoroughly tested as of the time of this writing. 
Unit tests rely under the [test module](https://github.com/quintoandar/hive-metastore-client/tree/main/tests/unit) 
and integration tests under the [integration_test module](https://github.com/quintoandar/hive-metastore-client/tree/main/tests/integration).
 [pytest](https://docs.pytest.org/en/latest/) is used to write all of this project's tests. 

**Before opening a PR, check if all your new code is 100% covered with tests.**

The `make tests` executes both integration and unit tests. But you can run just
 unit tests with the make command at the project's root:
```bash
make unit-tests
```

You can run the integration tests in the same fashion:
```bash
make integration-test
```

Style check is available through make too:
```bash
make style-check
```

## Documentation

### Updating generated documentation:
- First install requirements running `make requirements-docs`.
- To recreate .rst files run `make update-docs`. If a new module was added, edit docs/source/index.rst file to add the rst file for the module manually.
- To test the documentation generated run `make docs`. It will generate html documentation files in docs/build/html folder.


## GitFlow
Please **follow the guidelines** described [here](WORKFLOW.md).

## Pull Requests

Pull Request is, in summary, a request for changing code in a given repository.

They're are typically used by teams for shared collaboration and feature work or bug fixes. The idea is to make sure 
well written and bug-free code gets pushed to the repository. It is a way to develop high-quality code.

### Creating a Pull Request

Once you make changes you need in your code in the branch, you submit a PR. Once submitted, interested parties will 
perform a code review and provide you with any feedback/changes needed. So, it's important that your PR follow some 
principles:

#### Good branch name

First all, your branch name should be meaningful. Remember that this is the first description of your code change and 
anybody can checkout into your branch to use or review it.

There are two patterns to the branch name:

* camelCase: ```addPrGuidelines```
* kebab: ```add-create-pr``` (we prefer this one)

And a good practice in some repository is to follow the features/bugfixes branches: ```feature/add-create-pr```

#### Create small PRs

Before you start working on a story/feature, make a mental/written note on how you want to break it down into several smaller pull requests, so it's possible to define a sufficient narrow scope for your changes. Also do not forget to assign yourself regarding the PR.

#### Add good description

It is essential to have a good description of your PR, but.. what is a good description?

We usually consider a good description when it has:

* Explain the context of that feature/fix;
* Why and how it's done;
* Unit and integration tests, when applicable;

Basically, this can be achieved by simply following our PR template. :)

#### Add labels

In all project, we have different labels, like "WIP", "review", "bug", etc. Consider always adding the right label to make your reviewers' lives easier.
