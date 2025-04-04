# dict comprehension with four items
a = ['a', 'b', 'c', 'd', 'e']
b = [1,2,3,4,5]

my_dict = {x:y for (x,y) in zip(a, b)}

print(my_dict)