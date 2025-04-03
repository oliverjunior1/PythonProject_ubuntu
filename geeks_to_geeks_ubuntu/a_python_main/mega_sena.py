# mega
import random

def mega_sena():
    x = sorted(random.sample(range(1,61),6))
    return print(x)

print(mega_sena())