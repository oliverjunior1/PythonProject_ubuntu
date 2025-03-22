def args_and_kwargs(*args, **kwargs):
    print(f'args: {args} kwargs: {kwargs}')

args_and_kwargs(1,2,a=3, b=4)