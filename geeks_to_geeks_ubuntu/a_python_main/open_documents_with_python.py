x = open('message.txt', 'r')
y = x.read()
print(y)

with open('message2.txt', 'w') as file:
    file.write("God has been love the world, at some mode, who give your only son, for everybody who believes don't pain, but had the eternal life.")

a = open('message2.txt', 'r')
b = a.read()

print(b)