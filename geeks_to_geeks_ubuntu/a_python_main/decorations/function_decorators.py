# decorations without method
def fun1(x):
    def fun2():
        print("aaaaaaaaaa")
        x()
        print('bbbbbbbbb')
    return fun2

@fun1

def greetings():
    print("Hello")

greetings()