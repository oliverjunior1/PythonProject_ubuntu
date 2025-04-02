# family

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name is {self.name} Oliveira and the age {self.age} years old."

person = Person("Joao Pedro", 12)
person1 = Person("Mariane Vitória", 4)
person2 = Person("Joaquim", 42)
person3 = Person("Alyne", 38)

print(person)
print(person1)
print(person2)
print(person3)