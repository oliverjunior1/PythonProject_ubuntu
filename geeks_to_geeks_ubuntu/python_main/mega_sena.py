import random

def luck():
    x = random.sample(range(1,61), 6)
    y = sorted(x)
    return print(y)

luck()
