def add(x, y=8):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    """_summary_

    Args:
        x (_type_): _description_
        y (_type_): _description_

    Raises:
        ValueError: denominator is 0

    Returns:
        _type_: _description_
    """
    if y == 0:
        raise ValueError
    return x / y
