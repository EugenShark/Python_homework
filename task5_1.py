from itertools import count
from functools import reduce

my_list = []
for i in count(100, 2):
    if i > 1000:
        break
    else:
        my_list.append(i)


def my_func(prev_a, a):
    return prev_a * a


print(reduce(my_func, my_list))
