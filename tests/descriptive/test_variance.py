import pytest

from statio.descriptive.variance import variance


def test_variance_population():
    assert variance([1, 2, 3, 4, 5]) == 2.0


def test_variance_sample():
    assert variance([1, 2, 3, 4, 5], sample=True) == 2.5


def test_variance_single_value():
    assert variance([10]) == 0.0


def test_variance_decimal():
    assert variance([1.5, 2.5, 3.5]) == pytest.approx(2 / 3)


def test_variance_negative():
    assert variance([-2, -1, 0, 1, 2]) == 2.0


def test_variance_identical_values():
    assert variance([5, 5, 5, 5]) == 0.0


def test_variance_empty():
    with pytest.raises(ValueError):
        variance([])


def test_variance_invalid_container():
    with pytest.raises(TypeError):
        variance((1, 2, 3))


def test_variance_invalid_element():
    with pytest.raises(TypeError):
        variance([1, 2, "hello"])


def test_variance_none_element():
    with pytest.raises(TypeError):
        variance([1, None, 3])


def test_variance_sample_single_value():
    with pytest.raises(ValueError):
        variance([10], sample=True)


def test_variance_boolean_only():
    assert variance([True, False, True]) == pytest.approx(2 / 9)


def test_variance_mixed_boolean():
    with pytest.warns(UserWarning):
        result = variance([1, 2, True])

    assert result == pytest.approx(2 / 9)