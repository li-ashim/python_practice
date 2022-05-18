class SchoolMember:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def show(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


class Teacher(SchoolMember):
    def __init__(self, name: str, age: int, salary: int) -> None:
        super().__init__(name, age)
        self.salary = salary
    
    def show(self) -> str:
        return super().show() + f", Salary: {self.salary}"


class Student(SchoolMember):
    def __init__(self, name: str, age: int, grades: int) -> None:
        super().__init__(name, age)
        self.grades = grades
    
    def show(self) -> str:
        return super().show() + f", Grades: {self.grades}"


if __name__ == "__main__":
    # check if this code is working
    persons = [Teacher("Mr.Snape", 40, 3000), Student("Harry", 16, 75),
               SchoolMember("John", 29)]

    for person in persons:
        print(person.show())
