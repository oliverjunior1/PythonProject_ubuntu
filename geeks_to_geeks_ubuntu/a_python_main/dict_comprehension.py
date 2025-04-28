# dict comprehension with four items

x = ['a', 'b', 'c', 'd']
y = [1,2,3,4]

my_dict = {a:b for (a,b) in zip(x,y)}

print(my_dict)