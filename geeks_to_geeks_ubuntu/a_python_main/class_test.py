# big bang

class Big_bang:
    def __init__(self, character, comic_books):
        self.character = character
        self.comic_books = comic_books

    def __str__(self):
        return f"The character {self.character} has {self.comic_books} comic books in his bedroom."

big_bang1 = Big_bang("Sheldon", 15000)
big_bang2 = Big_bang("Leonard", 12357)
big_bang3 = Big_bang("Howard", 11001)
big_bang4 = Big_bang("Hajesh", 8008)

print(big_bang1)
print(big_bang2)
print(big_bang3)
print(big_bang4)