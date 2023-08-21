"""Sample unit test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

from python_anvil_encryption import utils


def describe_feet_to_meters():
    def when_integer():
        assert utils.feet_to_meters(42) == 12.80165

    def when_string():
        assert utils.feet_to_meters("hello") is None
