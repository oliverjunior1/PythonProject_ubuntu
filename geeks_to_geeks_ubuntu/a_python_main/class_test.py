# Two and a half man

class Two_and_a_half:
    def __init__(self, name, loves):
        self.name = name
        self.loves = loves

    def __str__(self):
        return f"The character {self.name} has {self.loves} in him bed!"

two_and = Two_and_a_half("Charlie", 5)
two_and1 = Two_and_a_half("Alan", -2)

print(two_and)
print(two_and1)