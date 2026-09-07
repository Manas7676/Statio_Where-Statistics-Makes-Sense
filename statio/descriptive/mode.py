import warnings


def mode(data):
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

    frequencies = {}

    for value in data:
        if value in frequencies:
            frequencies[value] = frequencies[value] + 1
        else:
            frequencies[value] = 1

    highest_frequency = max(frequencies.values())

    modes = []

    for value in frequencies:
        if frequencies[value] == highest_frequency:
            modes.append(value)

    return modes