# Big Bang

class Big_bang:
    def __init__(self, character, comic_books):
        self.character = character
        self.comic_books = comic_books

    def __str__(self):
        return f"The character {self.character} have {self.comic_books} comic books in his bedroom."

big_bang = Big_bang('Sheldon', 25000)
big_bang2 = Big_bang("Leonard", 20000)
big_bang3 = Big_bang('Howard', 15000)
big_bang4 = Big_bang('Hajesh', 8008)

print(big_bang)
print(big_bang2)
print(big_bang3)
print(big_bang4)