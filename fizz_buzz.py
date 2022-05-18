from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    """
    Create a function which generates and returns a list with numbers from 1 to `n` inclusive
    where the `n` is passed as a parameter to the function.
    But if the number is divided by 3 the function puts a `Fizz` word
    into the list, and if the number is divided by 5 the function puts
    a `Buzz` word into the list. If the number is divided both by 3 and 5 the function puts
    `FizzBuzz` into the list.
    """
    result = []

    for i in range(1, n+1):
        if (i % 15 == 0):
            result.append('FizzBuzz')
        elif (i % 3 == 0):
            result.append('Fizz')
        elif (i % 5 == 0):
            result.append('Buzz')
        else:
            result.append(i)
    
    return result

