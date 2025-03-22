class Big_bang:
    def __init__(self, name, comic_books):
        self.name = name
        self.comic_books = comic_books

    def __str__(self):
        return f"{self.name} has {self.comic_books} comic books in his bedroom."

big_bang = Big_bang("Sheldon", 10000)
big_bang2 = Big_bang("Leonard", 5500)

print(big_bang)
print(big_bang2)