class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfun(self):
        print("Hello my name is " + self.name)
        print("My age is", self.age)

p1 = Person("John", 36)

p1.myfun()