import random

def lotofacil():
    x = random.sample(range(1,26),15)
    y = sorted(x)
    return print(y)

lotofacil()