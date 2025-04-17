# dict comprehension with four items

a = ['a','b', 'c', 'd']
b = [1,2,3,4]

x = {c:d for c,d in zip(a, b)}

print(x)