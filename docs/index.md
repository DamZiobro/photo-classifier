photo-classifier
==

Extract data from your photos and show photos on map where taken

## Pre-install dependencies

1. [make](https://www.gnu.org/software/make/) - commands control tool
2. [poetry](https://python-poetry.org/) - requirements manager and virtualenv management tool
3. [python 3.8+](https://www.python.org/) - python pre-installed on your machine
4. [pre-commit](https://pre-commit.com/) - (optional) development dependency for checking code quality before commit

## Getting started

### Install pre-commit hooks

```
make pre-commit
```

### Create virtualenv and install dependencies

```
make deps
```

### Run app locally

One command `make run` for:
* creating virtualenv using `poetry` (one off action)
* install all the python [requirements](./pyproject.toml) inside the virtualenv (one off action)
* install CLI app locally inside virtualenv and run it


### Install app globally in the system and run

```
make install
photo-classifier --version
photo-classifier
```

### Code checks (static code analysis)

```
make lint
make cov
```

### Restart project from scratch

```
make clean
```

## Developer guide

### Project includes

* **[poetry](https://python-poetry.org/)-based dependency and virtual machines management**
* **[pytest](https://docs.pytest.org/en/7.3.x/)**-based unit tests with **code coverage report** and **HTML-based test report**
* **static code analysis (linting)** ([blake](https://github.com/psf/black), [isort](https://pycqa.github.io/isort/), [flake8](https://flake8.pycqa.org/en/latest/), [mypy](https://mypy.readthedocs.io/en/stable/))
* **CI/CD** including linting and unit tests checks (integrated with **[GitHub Actions](https://github.com/features/actions)** according to **[Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)** rules)
* **[Makefile](https://www.gnu.org/software/make/)** with most useful **preconfigured** development and CI/CD **commands**
* **[mkdocs](https://www.mkdocs.org/getting-started/)**-based automatically generated **documentation** (use `make docs` or `make docs-run`)
* **[pre-commit](https://pre-commit.com/)**-based code **checks during git commit**
* **[poetry](https://python-poetry.org/)-based** - **publishing to [PyPi](https://pypi.org/)**

### All dev commands

* **make help** - print descriptions of all make commands
* **make pre-commit** - install pre-commit hooks (see [.pre-commit-config.yaml](./.pre-commit-config.yaml))
* **make deps** - install project dependencies
* **make build** - build python distribution and wheels
* **make publish** - publish lib to the PyPI (pip repo)
    * `PYPI_USERNAME` and `PYPI_PASSWORD` env vars MUST be exported before publishing
    * if you would like to set **private PyPI (pip repo)** please set your repo URL to the `pypirepo` using: `poetry config repositories.pypirepo https://test.pypi.org/legacy/`
* **make docs** - generate mkdocs-based documentation and save to site/index.html
* **make docs-run** - run mkdocs-based doc in the local server
* **make format** - format code according to [PEP-8](https://peps.python.org/pep-0008/) style
* **make lint** - check wehther code is formatted according to [PEP-8](https://peps.python.org/pep-0008/) style
* **make run** - run the CLI app from locally installed virtualenv
* **make install** - install the CLI app into the system global path
* **make clean** - clean full project's virtualenv and dependencies
