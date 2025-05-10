# decorations with method
def fun1(x):
    def fun2(*args, **kwargs):
        print("aaaaaaaaaa")
        x(*args, **kwargs)
        print('bbbbbbbbbb')
    return fun2

@fun1
def greeting(name, age):
    print(f"Hello {name}")

greeting('Joaquim', 42)
