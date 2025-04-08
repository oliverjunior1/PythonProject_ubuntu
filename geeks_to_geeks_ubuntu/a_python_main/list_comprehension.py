# Three numbers  for 3
# problem 1: Make a list with some family members, that change to a list with name and last name.
family = ['Alyne', 'Mariane', 'Joaquim', 'Joao']

family_ln = [x + " Oliveira" for x in family]

print(family_ln)

# Withdraw from some list one list with only 'b'
fruits = ['apple', 'banana', 'bayberry', 'orange']

fruits_b = [x for x in fruits if 'b' in x]

print(fruits_b)
# multiply all the elements from a list for 5

