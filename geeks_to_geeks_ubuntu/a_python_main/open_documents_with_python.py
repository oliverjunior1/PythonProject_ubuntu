# read the text and write the text

x = open('message.txt', 'r')
y =x.read()
print(y)

with open('message2.txt', 'w') as file:
    file.write('Jesus give his own life for us sinners...')

a = open('message2.txt', 'r')
b = a.read()
print(b)