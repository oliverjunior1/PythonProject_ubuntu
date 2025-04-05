# dict comprehension with five items
a = ['a','b','c','d']
b = [1,2,3,4]

my_list= {x:y for (x,y) in zip(a,b)}

print(my_list)