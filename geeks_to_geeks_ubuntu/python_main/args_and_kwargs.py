def args_and_kwargs(*args, **kwargs):
    print(f"The args are: {args}")
    print(f"The kwargs are: {kwargs}")

# the args types can receive only one type, but the kwargs multiples types
args_and_kwargs(1,2,3,4, a = "Joao", b="Maria", c=5, d=5.5)