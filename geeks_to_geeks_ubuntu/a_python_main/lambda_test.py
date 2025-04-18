# Problem of rectangle area: yes
# with input: no
# lambda pow 2

side_1 = int(input('Enter the side 1: '))
side_2 = int(input('Enter the side 2: '))

area_rect = lambda x, y: x*y

print(f"The rectangle area is: {area_rect(side_1, side_2)} m2!")

