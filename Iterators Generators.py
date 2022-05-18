from typing import Generator, Iterable, Sequence


def custom_zip(*args: Sequence[Iterable]) -> Generator:
    if len(args) == 0:
        return
    min_length = min(map(len, args))

    for i in range(min_length):
        t = tuple((arg[i] for arg in args))
        yield (t)
