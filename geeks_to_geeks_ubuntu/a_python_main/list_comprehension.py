# four numbers  for 3
# problem 1: Make a list with some family members, that change to a list with name and last name.
from pygame.surfarray import pixels_red

family = ["Joao ", "Mariane ", "Alyne ", "Joaquim "]

f_oliveira = [x+'Oliveira' for x in family]

print(f_oliveira)

# Withdraw from some list one list with only 'a'

fruits = ['banana', 'apple', 'melon', 'lemon', 'watermelon']

fruits_a = [y for y in fruits if "a" in y]

print(fruits_a)

# multiply all the elements from a list for 4

list = [10,20,30,40]

list_for_4 = [z*4 for z in list]

print(list_for_4)