# read the text and write the text
# new text a)"He's called Emmanuel, and he brought peace to this world!"
# new text b)"God loved the world, from that manner, who give his son, for everybody who believe in him, don't perish, but have the eternal life."

a = open('message.txt', 'r')
b = a.read()
print(b)

with open('message2.txt', 'w') as file:
    file.write("God loved the world, from that manner, who give his son, for everybody who believe in him, don't perish, but have the eternal life.")

x = open('message2.txt', 'r')
y = x.read()
print(y)
