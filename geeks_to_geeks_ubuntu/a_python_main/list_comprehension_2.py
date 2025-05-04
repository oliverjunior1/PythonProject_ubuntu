# Withdraw from some list one list with only 'b'

fruits = ['banana', 'apple', 'melon', 'babaco']

fruits_b = [x for x in fruits if 'b' in x]

print(fruits_b)