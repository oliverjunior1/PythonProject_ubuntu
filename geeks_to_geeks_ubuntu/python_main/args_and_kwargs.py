def arg_kwargs(*args, **kwargs):
    print(f"args:{args} and kwargs: {kwargs}.")


arg_kwargs(1,2,3,4, a=5, b=6, c=7, d=8)
