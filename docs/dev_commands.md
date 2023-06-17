## All dev and run commands

* **make help** - print descriptions of all make commands
* **make pre-commit** - install pre-commit hooks (see [.pre-commit-config.yaml](../.pre-commit-config.yaml))
* **make deps** - install project dependencies
* **make build** - build python distribution and wheels
* **make publish** - publish lib to the PyPI (pip repo)
    * `PYPI_USERNAME` and `PYPI_PASSWORD` env vars MUST be exported before publishing
    * if you would like to set **private PyPI (pip repo)** please set your repo URL to the `pypirepo` using: `poetry config repositories.pypirepo https://test.pypi.org/legacy/`
* **make docs** - generate mkdocs-based documentation and save to site/index.html
* **make docs-run** - run mkdocs-based doc in the local server
* **make format** - format code according to [PEP-8](https://peps.python.org/pep-0008/) style
* **make lint** - check wehther code is formatted according to [PEP-8](https://peps.python.org/pep-0008/) style
* **make unit-tests** - run unit tests
* **make cov** - run unit tests and should code coverage
* **make cov-html** - run unit tests and generate HTML report showing code coverage
* **make checks** - run all code checks
* **make install** - install the CLI app into the system global path
* **make clean** - clean full project's virtualenv and dependencies
