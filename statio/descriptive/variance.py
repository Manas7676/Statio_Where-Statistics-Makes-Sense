import warnings


def variance(data, sample=False):
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if len(data) == 0:
        raise ValueError("data cannot be empty")

    has_boolean = False
    has_numeric = False

    for value in data:
        if isinstance(value, bool):
            has_boolean = True
        elif isinstance(value, (int, float)):
            has_numeric = True
        else:
            raise TypeError("all elements must be numeric")

    if has_boolean and has_numeric:
        warnings.warn(
            "Boolean value detected. True/False will be interpreted as 1/0.",
            UserWarning
        )

    count = len(data)

    if sample and count < 2:
        raise ValueError(
            "sample variance requires at least two values"
        )

    total = 0

    for value in data:
        total = total + value

    mean_value = total / count

    squared_deviations = 0

    for value in data:
        deviation = value - mean_value
        squared_deviations = squared_deviations + deviation ** 2

    if sample:
        return squared_deviations / (count - 1)

    return squared_deviations / count