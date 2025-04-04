# four numbers
def args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

args_and_kwargs(1,20,55,30)
args_and_kwargs(a=101, b=30, c=1000, d=505)