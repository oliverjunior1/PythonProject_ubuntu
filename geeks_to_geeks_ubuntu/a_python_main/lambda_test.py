#Problem area of the rectangle:yes
# lambda 2x

side_1 = int(input('Put the first side: '))
side_2 = int(input('Put the second side: '))

x = lambda a, b : a * b
print(f"The rect area is {x(side_1, side_2)} m2.")