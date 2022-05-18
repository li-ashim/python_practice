from typing import List
from functools import reduce


def count_words(sentences: List[str], word: str) -> int:
    return reduce(int.__add__, map(lambda s: s.count(word), sentences), 0)