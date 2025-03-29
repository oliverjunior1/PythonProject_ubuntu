class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name is {self.name} and the age is {self.age} years old."

person1 = Person("Mariane Vitória",4)
person2 = Person("Joao Pedro",12)

print(person1)
print(person2)

