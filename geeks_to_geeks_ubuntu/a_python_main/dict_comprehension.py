# dict comprehension with my own dates and four items

x = ['name', 'age', 'city', 'state']
y = ['Joaquim', 40, 'Anapolis', 'Goias']

my_dict= {a:b for (a,b) in zip(x,y)}

print(my_dict)