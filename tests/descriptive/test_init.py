from statio.descriptive import mean, median, mode, variance


def test_descriptive_api():
    assert mean([1, 2, 3]) == 2
    assert median([1, 2, 3]) == 2
    assert mode([1, 2, 2, 3]) == [2]
    assert variance([1, 2, 3]) == 2 / 3