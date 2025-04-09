# Four numbers  for 3
# problem 1: Make a list with some family members, that change to a list with name and last name.
family = ["Joaquim", "Alyne", "Joao", "Mariane"]

family_oliver = [x + " Oliveira" for x in family]

print(family_oliver)
# Withdraw from some list one list with only 'c'
fruits = ['cacao', 'orange', 'cherry', 'grape', 'crabapple']

fruits_c = [x for x in fruits if 'c' in x]

print(fruits_c)

# multiply all the elements from a list for 5

x = [1,2,3,4,5]

x_5 = [b**5 for b in x]

print(x_5)





