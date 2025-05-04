def fun1(x):
    def fun2(*args, **kwargs):
        print("aaaaaaa")
        x(*args, **kwargs)
        print("bbbbbbb")
    return fun2

@fun1
def greetings(name, age):
    print(f"Hello {name}, your age is {age} years old.")

greetings("Joaquim", 40)