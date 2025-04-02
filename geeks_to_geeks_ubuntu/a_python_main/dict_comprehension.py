# dict comprehension with five items
x = ['a', 'b', 'c', 'd', 'e']
y = [1,2,3,4,5]

my_dict = {a:b for (a,b) in zip(x,y)}

print(my_dict)