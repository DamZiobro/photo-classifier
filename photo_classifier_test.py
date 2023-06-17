"""Unit tests of photo-classifier."""

import pytest
from click.testing import CliRunner

from photo_classifier.cli import version


@pytest.fixture
def cli_runner():
    return CliRunner()


def test_version(cli_runner):
    """Verify version."""
    result = cli_runner.invoke(version)
    assert result.exit_code == 0
    assert result.output.strip() == "0.0.1"
