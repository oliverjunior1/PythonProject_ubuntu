# decorations without method
def fun1(x):
    def fun2():
        print("aaaaaaaaaa")
        x()
        print('bbbbbbbbbb')
    return fun2

@fun1
def greeting():
    print("Hello Joaquim")

greeting()
