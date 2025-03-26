class Big_bang_theory:
    def __init__(self, name, comic_book):
        self.name = name
        self.comic_book = comic_book

    def __str__(self):
        return f"The character {self.name} has {self.comic_book} comic-books in his bedroom."

character_1 = Big_bang_theory("Sheldon", 10000)
character_2 = Big_bang_theory("Leonard", 7000)
character_3 = Big_bang_theory("Howard", 6500)
character_4 = Big_bang_theory("Hajesh", 6498)

print(character_1)
print(character_2)
print(character_3)
print(character_4)