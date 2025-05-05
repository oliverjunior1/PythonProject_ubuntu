# two_and_a_half

class Two_and_a_half_man:
    def __init__(self, name, womans):
        self.name = name
        self.womans = womans

    def __str__(self):
        return f"The character {self.name} has {self.womans} womans in his bedroom."

character1 = Two_and_a_half_man("Charlie", 5)
character2 = Two_and_a_half_man("Alan", 0)

print(character1)
print(character2)