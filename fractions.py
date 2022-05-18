def get_fractions(a_b: str, c_b: str) -> str:
    """
    Create a function what takes two parameters of string type which are fractions and
    returns a sum expression of these fractions and the sum result.
    For example:
    >>> a_b = '1/3'
    >>> c_b = '5/3'
    >>> get_fractions(a_b, c_b)
    '1/3 + 5/3 = 6/3'
    """
    a = int(a_b.split('/')[0])
    c = int(c_b.split('/')[0])
    b = a_b.split('/')[1]

    return f'{a_b} + {c_b} = {a + c}/{b}'
