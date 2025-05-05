# decorations without method
def fun1(x):
    def fun2():
        print("#####winner#######")
        x()
        print('###################')
        print()
    return fun2

@fun1
def greetings():
    print("Joaquim Rodrigues")

greetings()