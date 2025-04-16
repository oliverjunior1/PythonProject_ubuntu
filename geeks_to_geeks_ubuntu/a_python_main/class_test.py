# family

class Family:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'The name is {self.name} and the age is {self.age} years old!'

family = Family("Joao Pedro", 12)
family1 = Family('Mariane Vitória',4 )
family2 = Family('Alyne Oliveira',39 )
family3 = Family('Joaquim Rodrigues',42 )

print(family)
print(family1)
print(family2)
print(family3)