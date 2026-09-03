import pytest

from statio.descriptive.mean import mean


def test_mean_basic():
    assert mean([10, 20, 30, 40]) == 25.0


def test_mean_decimal():
    assert mean([1.5, 2.5, 3.5]) == 2.5


def test_mean_negative():
    assert mean([-10, 20, 30]) == 13.333333333333334


def test_mean_single_value():
    assert mean([10]) == 10.0


def test_mean_boolean_only():
    assert mean([True, False, True]) == 2 / 3


def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])


def test_mean_invalid_container():
    with pytest.raises(TypeError):
        mean((1, 2, 3))


def test_mean_invalid_element():
    with pytest.raises(TypeError):
        mean([1, 2, "hello"])


def test_mean_none_element():
    with pytest.raises(TypeError):
        mean([1, None, 3])