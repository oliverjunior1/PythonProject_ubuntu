x = open('message.txt', 'r')
y = x.read()

print(y)

with open('message2.txt', 'w') as file:
    file.write('Jesus is the way, the truth and the life.\n')

a = open('message2.txt', 'r')
b = a.read()

print(b)

