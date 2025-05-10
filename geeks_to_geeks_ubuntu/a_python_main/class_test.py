# Big Bang

class Big_Bang:
    def __init__(self, character, comic_book):
        self.character = character
        self.comic_book = comic_book

    def __str__(self):
        return f"The character has {self.character} has {self.comic_book} in his bedroom."

character1 = Big_Bang("Sheldon", 25000)
character2 = Big_Bang("Leonard", 18000)
character3 = Big_Bang("Howard", 12012)
character4 = Big_Bang("Hajesh", 8008)

print(character1)
print(character2)
print(character3)
print(character4)