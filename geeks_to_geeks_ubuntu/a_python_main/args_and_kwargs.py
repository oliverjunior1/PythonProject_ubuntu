# five numbers
def args_kwargs(*args, **kwargs):
    print(f"args:{args} and kwargs: {kwargs}!")

args_kwargs(1,2,3,4,5, a=1, b=2, c=3, d=4, e=5)