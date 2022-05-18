class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if (value < 0) or (value > 100):
            raise ValueError
        instance.__dict__[self.name] = value
    
    def __set_name__(self, owner, name):
        self.name = name


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if (self.name in instance.__dict__):
            raise ValueError
        instance.__dict__[self.name] = value
    
    def __set_name__(self, owner, name):
        self.name = name


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price) -> None:
        self.author = author
        self.name = name
        self.price = price