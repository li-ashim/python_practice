def my_reduce(func, iter):
    """
    Applies `func` to reduce values in `iter` iterable
    to one value.
    """
    assert len(iter) > 1, 'Iterable must have at least 2 values'

    res = iter[0]
    for i in range(1, len(iter)):
        res = func(res, iter[i])

    return res