# family

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name is {self.name} and the age is {self.age} years old."

person1 = Person("Joaquim", 42)
person2 = Person("Alyne", 39)
person3 = Person("Joao", 12)
person4 = Person("Mariane", 4)

print(person1)
print(person2)
print(person3)
print(person4)
