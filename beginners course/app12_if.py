in_cuhk = False
is_male = False


if in_cuhk:
    print("You are Siu or Yin.")
elif is_male:
    print("You are Fung.")
else:
    print("Nobody.")

NOOOOOOOOO, cant deduce its Yin, because theres a non-existing situaion
if not is_male:
    print("You are Yin.")
elif in_cuhk:
    print("You are Siu.")
elif is_male:
    print("You are Fung.")
else:
    print("Nobody.")

if in_cuhk and is_male:
    print("You are Siu.")
elif in_cuhk and not is_male:
    print("You are Yin.")
else:
    print("You are Fung.")
