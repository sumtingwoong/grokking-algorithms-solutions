# Need to write the sum of a list using only recursion

from random import randint


def rec_sum(mass: list) -> int:
    if len(mass) == 0:
        return 0
    elif len(mass) == 1:
        return mass[0]
    else:
        return mass[0] + rec_sum(mass[1:])


random_list = [randint(0, 50) for i in range(randint(0, 10))]
print(random_list)
print(rec_sum(random_list))
