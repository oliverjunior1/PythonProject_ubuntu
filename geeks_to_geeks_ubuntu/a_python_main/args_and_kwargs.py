# four numbers
def args_and_kwargs(*args, **kwargs):
    print(f"args: {args}, kwargs: {kwargs}")

args_and_kwargs(1,2,3,4, a=10, b=20, c=30, d=40)