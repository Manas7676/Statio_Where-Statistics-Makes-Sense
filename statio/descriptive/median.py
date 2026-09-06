import warnings


def median(data):
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

    ordered_data = sorted(data)

    count = len(ordered_data)

    if count % 2 == 1:
        middle_index = count // 2
        return ordered_data[middle_index]

    middle_index = count // 2
    left_middle = ordered_data[middle_index - 1]
    right_middle = ordered_data[middle_index]

    return (left_middle + right_middle) / 2