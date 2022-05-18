class Adult:
    def __init__(self, age) -> None:
        self.age = age

    @property
    def age(self):
        print('Getting age...')
        return self._age
    
    @age.setter
    def age(self, age):
        print('Setting age...')
        if (age < 18):
            raise ValueError('Not really an adult!')
        self._age = age

a1 = Adult(43)
a1.age
a2 = Adult(15)