class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
p2 = Person("Hari", 19)

print(p1.name)
print(p1.age)
print(p2.name, p1.name) 