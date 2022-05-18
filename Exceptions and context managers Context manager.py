import os
from contextlib import contextmanager


@contextmanager
def cd_context(path: str):
    if (not os.path.exists(path) or not os.path.isdir(path)):
        raise ValueError
    old_dir = os.getcwd()
    try:
        os.chdir(path)
        new_dir = os.getcwd()
        yield new_dir
    finally:
        os.chdir(old_dir)

