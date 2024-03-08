from random import randint as ri


def die(size: int):
    """
    :param size: how many faces the dice has
    :return: result of rolling the dice
    """
    if size <= 1 or type(size) != int:  # ensure sides is an Int and is at least 2
        raise ValueError("Die must have at least 2 sides")
    return ri(1, size)
