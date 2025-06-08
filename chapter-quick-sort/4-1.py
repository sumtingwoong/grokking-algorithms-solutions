def rec_sum(mass: list):
    if len(mass) == 0:
        return 0
    elif len(mass) == 1:
        return mass[0]
    else:
        return mass[0] + rec_sum(mass[1:])


print(rec_sum([2, 4, 6, 10]))
