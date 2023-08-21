"""Sample integration test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

import pytest
from click.testing import CliRunner

from python_anvil_encryption.cli import main


@pytest.fixture
def runner():
    return CliRunner()


def describe_cli():
    def describe_conversion():
        def when_integer(runner):
            result = runner.invoke(main, ["42"])

            assert result.exit_code == 0
            assert result.output == "12.80165\n"

        def when_invalid(runner):
            result = runner.invoke(main, ["foobar"])

            assert result.exit_code == 0
            assert result.output == ""
