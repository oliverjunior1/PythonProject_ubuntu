
x = open('message.txt', 'r')
y = x.read()
print(y)

with open('message2.txt', 'w') as file:
    file.write("Jesus is the salt of the earth and the light of the World!")

a = open('message2.txt', 'r')
b = a.read()
print(b)