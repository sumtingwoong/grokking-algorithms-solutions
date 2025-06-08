# Need to find the max of the list using recursion

from random import randint


def get_max(mass: list) -> int:
    if len(mass) == 2:
        return mass[0] if mass[0] > mass[1] else mass[1]
    current_max = get_max(mass[1:])
    return current_max if current_max > mass[0] else mass[0]


random_list = [randint(0, 50) for i in range(randint(2, 10))]
print(random_list)
print(get_max(random_list))
