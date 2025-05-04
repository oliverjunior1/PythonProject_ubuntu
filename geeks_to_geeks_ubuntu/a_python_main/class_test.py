# big bang

class Big_bang:
    def __init__(self, character, comic_books):
        self.character = character
        self.comic_books = comic_books

    def __str__(self):
        return f"The character {self.character} has {self.comic_books} comic books in his bedroom."

character1 = Big_bang("Sheldon", 20000)
character2 = Big_bang("Leonard", 17000)
character3 = Big_bang("Howard", 12588)
character4 = Big_bang("Hajesh", 8008)

print(character1)
print(character2)
print(character3)
print(character4)