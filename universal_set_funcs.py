def intersect(first, *args) -> set:
    res = set(first)
    for arg in args:
        res = res.intersection(set(arg))
    
    return res

s1 = {1, 2 ,3 ,4, 5}
s2 = {2 ,3 ,4, 5, 6}
s3 = {3 ,4, 5, 6, 7}


def union(first, *args) -> set:
    res = set(first)
    for arg in args:
        res |= arg
    
    return res
