import random

def mega_s():
    x = random.sample(range(1,61), 6)
    y = sorted(x)
    return print(y)

mega_s()
