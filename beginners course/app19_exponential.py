def raise_to_power(base_num, power_num):
    return base_num ** power_num


print(raise_to_power(2, 4))


def raise_to_power(base_num, power_num):
    n = 1
    for index in range(power_num):
        n *= base_num
    return n


print(raise_to_power(22, 5))
