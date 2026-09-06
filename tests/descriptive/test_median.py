import pytest

from statio.descriptive.median import median


def test_median_odd():
    assert median([7, 2, 9, 4, 5]) == 5


def test_median_even():
    assert median([10, 2, 8, 4]) == 6


def test_median_single_value():
    assert median([100]) == 100


def test_median_negative():
    assert median([-5, -10, 20, 0, -2]) == -2


def test_median_decimal():
    assert median([1.5, 3.5, 2.5]) == 2.5


def test_median_duplicates():
    assert median([1, 2, 2, 2, 100]) == 2


def test_median_empty():
    with pytest.raises(ValueError):
        median([])


def test_median_invalid_container():
    with pytest.raises(TypeError):
        median((1, 2, 3))


def test_median_invalid_element():
    with pytest.raises(TypeError):
        median([1, 2, "hello"])


def test_median_none_element():
    with pytest.raises(TypeError):
        median([1, None, 3])


def test_median_boolean_only():
    assert median([True, False, True]) == 1


def test_median_mixed_boolean():
    with pytest.warns(UserWarning):
        result = median([10, 20, True])

    assert result == 10