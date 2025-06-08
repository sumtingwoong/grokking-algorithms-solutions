# Need to write the sum of a list using only recursion

from random import randint


def get_sum(mass: list) -> int:
    if not mass:
        return 0
    return mass[0] + get_sum(mass[1:])


random_list = [randint(0, 50) for i in range(randint(0, 10))]
print(random_list)
print(get_sum(random_list))
