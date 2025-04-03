
x = open('message.txt', 'r')
y = x.read()

print(y)

with open('message2.txt', 'w') as file:
    file.write('Jesus is the king of the kings and the Lord of the Lords.')

x = open('message2.txt', 'r')
y = x.read()
print(y)