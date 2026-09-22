from statio.descriptive import mean, median, mode, variance


def test_descriptive_functions_are_available():
    assert callable(mean)
    assert callable(median)
    assert callable(mode)
    assert callable(variance)


def test_descriptive_functions_work_together():
    data = [1, 2, 2, 3, 4]

    assert mean(data) == 2.4
    assert median(data) == 2
    assert mode(data) == [2]
    assert variance(data) == 1.04