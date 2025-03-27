class Person:
    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age

    def __str__(self):
        return f"The name is {self.name} {self.lname} and the age is {self.age} years old."

person1 = Person("Joao", "Pedro", 12)
person2 = Person("Mariane", "Vitoria", 4)

print(person1)
print(person2)