# x = [1,2,3,4,5,6,7,8]
#
# y = [(a**2)/5 for a in x]
#
# print(y)

names = ["Joao", "Joaquim", "Alyne", "José", "Davelina", "Zélia"]

search_letter = input("Put a letter to search in names: ").capitalize()
names_j = [x for x in names if f"{search_letter}" in x]

print(names_j)