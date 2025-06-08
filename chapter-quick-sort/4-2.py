# Need to find the length of the list using recursion

from random import randint


def get_len(mass: list) -> int:
    if not mass:
        return 0
    return 1 + get_len(mass[1:])


random_list = [randint(0, 50) for i in range(randint(0, 10))]
print(random_list)
print(get_len(random_list))
