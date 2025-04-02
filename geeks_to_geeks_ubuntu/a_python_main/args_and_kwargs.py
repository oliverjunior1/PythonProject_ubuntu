# four numbers
def args_kwargs(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

args_kwargs(1,2,3,4)
args_kwargs(a=1, b=2, c=3, d=4)

