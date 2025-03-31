def args_and_kwargs(*args, **kwargs):
    return print(f"The args are: {args}, the kwargs are: {kwargs}")

args_and_kwargs(1,2,3,4,5,6,7,a=1, b=2, c=3, d=4)
args_and_kwargs(100,200, a=100, b=200)