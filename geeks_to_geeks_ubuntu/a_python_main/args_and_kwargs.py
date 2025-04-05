# five numbers
def kwargs_and_args(*args, **kwargs):
    print(args)
    print(kwargs)

kwargs_and_args(1,2,3,4,5)
kwargs_and_args(a=1, b=2, c=3, d=4, e=5)