def input_num(n):
    while True:
        try:
            user_input = int(input(n))
        except ValueError:
            print("Please enter correctly.")
            continue
        else:
            if 10 >= user_input >= 1:
                return user_input
                break
            else:
                print("Please enter correctly.")
                continue


def print_board(i):
    for line in range(1, i + 1):
        start_num = i - line + 1
        print(str(start_num), end=" ")
        x = start_num
        reach_1 = False
        if x == 1:
            reach_1 = True
        for item in range(1, i):
            if item == start_num:
                reach_1 = True
            if not reach_1:
                x -= 1
                print(str(x), end=" ")
            if reach_1:
                x += 1
                print(str(x), end=" ")
        print("")


input_number = input_num("Enter an integer from 1 to 10: ")
print_board(input_number)