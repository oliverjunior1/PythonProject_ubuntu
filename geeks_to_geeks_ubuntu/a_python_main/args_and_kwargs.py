#four arguments

def args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

args_and_kwargs(1,2,3,4,a=1,b=2, c=3, d=4)
