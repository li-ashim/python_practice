class Field:
    def __init__(self):
        self.__value = None
    
    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value = new_value


if __name__ == "__main__":
    # Check if this code is working
    field = Field()
    field.set_value(123)
    print(field.get_value())
