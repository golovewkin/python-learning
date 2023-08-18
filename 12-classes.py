class Person:
    def __init__(self, name, age):  # self can be named any thing you like def __init__(mysillyobject, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# inheritance
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        # or use super
        # super().__init__(fname, lname)
