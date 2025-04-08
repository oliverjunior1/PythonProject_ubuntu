# dict comprehension with four items
a = ['a', 'b', 'c', 'd']
b = [10,20,30,40]

x = {y:z for (y,z) in zip(a, b)}

print(x)