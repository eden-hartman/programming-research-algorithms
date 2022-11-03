import inspect


def f(x: int, y: float, z):
    """ this function gets three variables and return their sum """
    return x + y + z


def safe_call(func, **kwargs):
    """ this function gets another function and args for it
        >>> safe_call(f, x=1, y=1.1, z=2)
        4.1
        >>> safe_call(f, x=1, y=1.5, z=2)
        4.5
        >>> safe_call(f, x=1, y=1, z=2)
        Traceback (most recent call last):
        ...
        Exception: invalid arg type: y, expected <class 'float'> and got <class 'int'>
    """
    args = inspect.getfullargspec(func).args
    annotations = inspect.getfullargspec(func).annotations
    for a in args:
        if a in annotations.keys() and annotations[a] is not type(kwargs[a]):
            raise Exception(f"invalid arg type: {a}, expected {annotations[a]} and got {type(kwargs[a])}")
    print(f(**kwargs))


if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)

    # safe_call(f, x=1, y=2, z=3)
    safe_call(f, x=1, y=1.1, z=2)