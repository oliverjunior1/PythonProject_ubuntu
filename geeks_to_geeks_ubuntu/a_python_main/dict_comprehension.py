# dict comprehension with five items
a = ['a', 'b', 'd', 'e', 'f']
b = [1,2,3,4,5]

my_dict = {x:y for (x,y) in zip(a, b)}

print(my_dict)