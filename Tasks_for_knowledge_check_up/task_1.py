from typing import Sequence, Iterator

class my_range:
    
    def __init__(self, *args: Sequence[int]) -> None:
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"{arg.__class__.__name__} object "
                                "cannot be interpreted as an integer")
                
        self.start = 0
        self.step = 1
        if len(args) == 1:
            self.stop, = args
        elif len(args) == 2:
            self.start, self.stop = args
        elif len(args) == 3:
            self.start, self.stop, self.step = args
            if self.step == 0:
                raise ValueError("arg 3 must not be zero")
        else:
            raise TypeError("my_range expected at most 3 arguments, "
                            f"got {len(args)}")
        self.val = self.start
            
    def __iter__(self) -> Iterator:
        return MyRangeIter(self.start, self.stop, self.step)
    
    
class MyRangeIter:
    
    def __init__(self, start, stop, step) -> None:
        self.start = start
        self.stop = stop
        self.step = step
        self.val = self.start
    
    def __next__(self) -> int:
        if ((self.step > 0 and self.val >= self.stop) or
            (self.step < 0 and self.val <= self.stop)):
            raise StopIteration
        value = self.val
        self.val += self.step
        return value
    
                
def test(my_range):
    assert list(my_range(5, 100, 2)) == list(range(5, 100, 2)), "1"
    assert list(my_range(10, 0, -2)) == list(range(10, 0, -2)), "2"
    assert list(my_range(10)) == list(range(10)), "3"
    assert list(my_range(10, 20)) == list(range(10, 20)), "4"
    assert list(my_range(-5, 5)) == list(range(-5, 5)), "5"
    assert list(my_range(-10, -20, -1)) == list(range(-10, -20, -1)), "6"
    assert list(my_range(-10, -20, 1)) == list(range(-10, -20, 1)), "7"
    assert list(my_range(10, 0, 1)) == list(range(10, 0, 1)), "8"
    assert next(iter(my_range(-10, -20, -1))) \
            == next(iter(range(-10, -20, -1))), "9"
    assert (iter(my_range(5)) is not my_range(5)) \
            == (iter(range(5)) is not range(5)), "10"
    print("All tests passed!\n")
            