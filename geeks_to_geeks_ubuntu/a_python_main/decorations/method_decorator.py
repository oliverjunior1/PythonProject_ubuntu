def fun1(x):
    def fun2(*args, **kwargs):
        print("######winner########")
        x(*args, **kwargs)
        print("####################")
        print()
    return fun2

@fun1
def greetings(name, age):
    print(f"{name} and {age} years old")

greetings("Joaquim", 40)
greetings("Alyne", 38)
greetings("Joao", 12)
greetings("Mariane", 4)


