# Family

class Family:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name is {self.name} and the age is {self.age} years old."

member1 = Family("Joao Pedro", 12)
member2 = Family("Mariane Vitória", 4)

print(member1)
print(member2)