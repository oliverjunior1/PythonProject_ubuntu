def args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

args_kwargs(1,2,a=10, b=20)
args_kwargs(100,200, a=2, b=5)