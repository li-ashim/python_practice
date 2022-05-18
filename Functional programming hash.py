from typing import List


def hash_names(names: List[str]) -> List[int]:
    """Returns hashes of provided names."""
    return list(map(hash, names))