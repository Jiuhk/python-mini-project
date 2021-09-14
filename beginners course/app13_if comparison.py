def have_2(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    if num1_str.count("2") > 0 and num2_str.count("2") == 0:
        return num1
    elif num2_str.count("2") > 0 and num1_str.count("2") == 0:
        return num2
    elif num2_str.count("2") > 0 and num1_str.count("2") > 0:
        return num1, num2


print(have_2(483238, 14234))


def have_2(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    if num1_str.count("2") > 0:
        print(num1)
    if num2_str.count("2") > 0:
        print(num2)
    else:
        return num1, num2


have_2(483238, 14234)


def have_2(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    lst = []
    if num1_str.count("2") > 0:
        lst.append(num1)
    if num2_str.count("2") > 0:
        lst.append(num2)
    return lst


print(have_2(483238, 1434))
