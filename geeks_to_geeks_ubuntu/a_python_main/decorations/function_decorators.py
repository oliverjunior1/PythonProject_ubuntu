def func1(x):
    def func2():
        print("aaaaaa")
        x()
        print("bbbbbbb")
    return func2

@func1

def greeting():
    print("Hello")

greeting()