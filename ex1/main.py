import inspect


def f(x: int, y: float, z):
    """ this function gets three variables and return their sum """
    return x + y + z


def safe_call(func, **kwargs):
    args = inspect.getfullargspec(func).args
    annotations = inspect.getfullargspec(func).annotations
    for a in args:
        if a in annotations.keys() and annotations[a] is not type(kwargs[a]):
            raise Exception(f"invalid arg type: {a}, expected {annotations[a]} and got {type(kwargs[a])}")
    print("all good")
    print(f(**kwargs))


if __name__ == "__main__":
    # safe_call(f, x=1, y=2, z=3)
    safe_call(f, x=1, y=2.2, z=3)
