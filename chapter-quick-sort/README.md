# Solutions to problems from chapter 4


## Quick sorting algorithm
```
from random import randint


def q_sort(mass: list) -> list:
    if len(mass) < 2:
        return mass
    support = mass[0]
    less = [i for i in mass[1:] if i < support]
    greater = [i for i in mass[1:] if i > support]
    return q_sort(less) + [support] + q_sort(greater)


random_list = [randint(0, 50) for i in range(randint(2, 10))]
print(random_list)
print(q_sort(random_list))
```
