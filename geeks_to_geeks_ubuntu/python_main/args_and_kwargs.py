def args_kwargs(*args, **kwargs):
    print(f"args: {args}, kwargs: {kwargs}.")

args_kwargs(1,2,3, a=4, b=5, c=6)