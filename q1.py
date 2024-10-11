import random
from random import choice

# a
list_T_F: list[bool] = [random.choice([True, False]) for _ in range(3)]
print(list_T_F)

# b
print('if all list is True ?', all(list_T_F))

# c
print('at least 1 True in the list ?', any(list_T_F))

# d
print('if all list is False ?', all(not value for value in list_T_F))

# e
print('at least 1 False list in the list ?', any(not value for value in list_T_F))

# f
list_random: list[int] = [random.randint(-2, 2) for _ in range(5)]
print(list_random)

# g
print('not all zero:',  all(num != 0 for num in list_random))

# h
print('at least 1 not zero:',  any(num != 0 for num in list_random))

# i
print('all list only is zero' , all(num == 0 for num in list_random))

# j
print('at least 1 zero' , any(num == 0 for num in list_random))
