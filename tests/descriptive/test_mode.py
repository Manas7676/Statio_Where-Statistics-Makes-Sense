import pytest

from statio.descriptive.mode import mode


def test_mode_single():
    assert mode([1, 2, 2, 3]) == [2]


def test_mode_multiple():
    assert mode([1, 1, 2, 2, 3]) == [1, 2]


def test_mode_all_unique():
    assert mode([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_mode_negative():
    assert mode([-2, -2, -1, 0, 0, 0]) == [0]


def test_mode_decimal():
    assert mode([1.5, 2.5, 2.5, 3.5]) == [2.5]


def test_mode_duplicates():
    assert mode([10, 10, 10, 20, 20, 30]) == [10]


def test_mode_single_value():
    assert mode([100]) == [100]


def test_mode_empty():
    with pytest.raises(ValueError):
        mode([])


def test_mode_invalid_container():
    with pytest.raises(TypeError):
        mode((1, 2, 2))


def test_mode_invalid_element():
    with pytest.raises(TypeError):
        mode([1, 2, "hello"])


def test_mode_none_element():
    with pytest.raises(TypeError):
        mode([1, None, 3])


def test_mode_boolean_only():
    assert mode([True, False, True]) == [True]


def test_mode_mixed_boolean():
    with pytest.warns(UserWarning):
        result = mode([1, 1, 2, True])

    assert result == [1]