class Big_bang:
    def __init__(self, character, comic_book):
        self.character = character
        self.comic_book= comic_book

    def __str__(self):
        return f'The character {self.character} has {self.comic_book} comic books in his bedroom.'

big_bang = Big_bang('Sheldon', 15155)
big_bang1 = Big_bang('Hajesh',10580)
big_bang2 = Big_bang('Leonard', 12800)
big_bang3 = Big_bang('Howard', 11500)

print(big_bang)
print(big_bang2)
print(big_bang1)
print(big_bang3)