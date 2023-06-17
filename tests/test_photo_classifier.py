"""Unit tests of photo-classifier."""

import pytest

from click.testing import CliRunner

from photo_classifier.cli import (
    version,
    classify_dirs,
)


@pytest.fixture
def cli_runner():
    return CliRunner()

def test_version(cli_runner):
    """Verify version."""
    result = cli_runner.invoke(version)
    assert result.exit_code == 0
    assert result.output.strip() == "0.0.1"


def test_photo_classifier_returns_text(cli_runner):
    """Verify output of fetch function."""
    result = cli_runner.invoke(classify_dirs)
    assert result.exit_code == 0
    assert result.output.strip() == "Classifying photos into dirs"

