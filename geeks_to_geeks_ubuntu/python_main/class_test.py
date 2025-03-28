class Big_bang_theory:
    def __init__(self, character, comic_books):
        self.character = character
        self.comic_books = comic_books

    def __str__(self):
        return f"The character {self.character} has {self.comic_books} comic-books in his bedroom!"

big_bang = Big_bang_theory("Sheldon", 10000)
big_bang2 = Big_bang_theory("Leonard", 8537)
big_bang3 = Big_bang_theory("Rajesh", 7350)

print(big_bang)
print(big_bang2)
print(big_bang3)