def func1(func):
    def func2():
        print("Hello 1")
        func()
        print("Hello 2")
    return func2

@func1

def greetings():
    print("Hello 3")

greetings()