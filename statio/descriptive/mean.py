import warnings


def mean(data):
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

    total = 0

    for value in data:
        total = total + value

    count = len(data)

    return total / count