def args_kwargs(*args, **kwargs):
    return print(f'Args: {args}, Kwargs: {kwargs}')

args_kwargs(1,2, a=3, b=4)