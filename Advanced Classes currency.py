from __future__ import annotations
from typing import Type
from functools import total_ordering
from abc import ABC, abstractmethod

@total_ordering
class Currency:
    """
    1 EUR = 2 USD = 100 RUB

    1 EUR = 2 USD    ;  1 EUR = 100 RUB
    1 USD = 0.5 EUR  ;  1 USD = 50 RUB
    1 RUB = 0.02 USD ;  1 RUB = 0.01 EUR
    """

    def __init__(self, value: float):
        self.value = float(value)

    _abbr = None
    
    _course = {'EUR': {'USD': 2.0, 'RUB': 100.0},
               'USD': {'EUR': 0.5, 'RUB': 50.0},
               'RUB': {'EUR': 0.01, 'USD': 0.02}}


    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        if cls == other_cls:
            return f'1 {cls._abbr} for 1 {cls._abbr}'
        return (f'{cls._course[cls._abbr][other_cls._abbr]} ' 
                f'{other_cls._abbr} for 1 {cls._abbr}')


    def to_currency(self, other_cls: Type[Currency]) -> Type[Currency]:
        if self.__class__ == other_cls:
            return other_cls(self.value)
        
        change_course = other_cls._course[self._abbr][other_cls._abbr]
        return other_cls(self.value * change_course)


    def __add__(self, other):
        if self.__class__ != other.__class__:
            change_course = other._course[other._abbr][self._abbr]
            other_val = other.value * change_course
        else:
            other_val = other.value

        return self.__class__(self.value + other_val)


    def __lt__(self, other) -> bool:
        if self.__class__ != other.__class__:
            change_course = other._course[other._abbr][self._abbr]
            other_val = other.value * change_course
        else:
            other_val = other.value

        return self.value < other_val

    def __eq__(self, other: Type[Currency]) -> bool:
        if self.__class__ != other.__class__:
            change_course = other._course[other._abbr][self._abbr]
            other_val = other.value * change_course
        else:
            other_val = other.value

        return self.value == other_val
        

    def __str__(self):
        return f'{self.value} {self._abbr}'



class Euro(Currency):
    _abbr = 'EUR'



class Dollar(Currency):
    _abbr = 'USD'



class Rubble(Currency):
    _abbr = 'RUB'



# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# Reference solution
@total_ordering
class Currency(ABC):
    
    @property
    @abstractmethod
    def label(self):
        pass
    
    @property
    @abstractmethod
    def usd_rate(self):
        pass
    
    def __init__(self, value: int):
        self.value = value
    
    def __add__(self, other):
        new_val = self.value + other.to(self.__class__).value
        return self.__class__(new_val)
    
    def __radd__(self, other):
        new_val = self.value + other
        return self.__class__(new_val)
    
    def __eq__(self, other):
        return self._usd_val == other._usd_val
    
    def __lt__(self, other):
        return self._usd_val < other._usd_val
    
    def __repr__(self):
        return f"{self.value} {self.label}"
    
    @property
    def _usd_val(self) -> int:
        return self.value * self.usd_rate
    
    @classmethod
    def course(cls, other_cls) -> str:
        return f"{cls(1).to(other_cls)} for 1 {cls.label}"
    
    def to(self, other_cls) -> "Currency":
        new_currency_val = self._usd_val / other_cls.usd_rate
        return other_cls(new_currency_val)


class Euro(Currency):
    label = "EUR"
    usd_rate = 2 # 1EUR == 2USD


class Dollar(Currency):
    label = "USD"
    usd_rate = 1 # 1USD == 1USD


class Rubble(Currency):
    label = "RUB"
    usd_rate = 0.02 # 1RUB == 0.02USD
