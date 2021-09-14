import random

def num_input():
    while True:
        try:
            r1, g1, b1, r2, g2, b2 = input("Enter six positive values separated by space: ").split()
            r1 = int(r1)
            g1 = int(g1)
            b1 = int(b1)
            r2 = int(r2)
            g2 = int(g2)
            b2 = int(b2)
            if r1 < 0 or r2 < 0 or g1 < 0 or g2 < 0 or b1 < 0 or b2 < 0:
                print("Please enter positive values.")
                continue
            else:
                return r1, g1, b1, r2, g2, b2
        except ValueError:
            print("Please enter correctly.")
            pass


def game(r1, g1, b1, r2, g2, b2, turn):
    while True:
        if turn == 0:
            if r1 + g1 + b1 == 1:
                r1 += 1
            elif r1 + g1 + b1 == 0:
                r1 += 2
            ball_list_0 = []
            for i in range(r1):
                ball_list_0.append("R")
            for i in range(g1):
                ball_list_0.append("G")
            for i in range(b1):
                ball_list_0.append("B")
            ball_a_0, ball_b_0 = random.choices(ball_list_0, k=2)
            if ball_a_0 == "R":
                r1 -= 1
            elif ball_a_0 == "G":
                g1 -= 1
            elif ball_a_0 == "B":
                b1 -= 1
            if ball_b_0 == "R":
                r1 -= 1
            elif ball_b_0 == "G":
                g1 -= 1
            elif ball_b_0 == "B":
                b1 -= 1
            if ball_a_0 == ball_b_0:
                if ball_a_0 == "R":
                    r2 += 1
                elif ball_a_0 == "G":
                    g2 += 1
                elif ball_a_0 == "B":
                    b2 += 1
            elif ball_a_0 != ball_b_0:
                if ball_a_0 != ball_b_0 != "R":
                    r2 += 1
                elif ball_a_0 != ball_b_0 != "G":
                    g2 += 1
                elif ball_a_0 != ball_b_0 != "B":
                    b2 += 1
            turn += 1
            if r1 + g1 + b1 == 1 and r2 + g2 + b2 == 0:
                if r1 == 1:
                    return "R"
                elif g1 == 1:
                    return "G"
                elif b1 == 1:
                    return "B"
        elif turn == 1:
            if r2 + g2 + b2 == 1:
                r2 += 1
            elif r2 + g2 + b2 == 0:
                r2 += 2
            ball_list_1 = []
            for i in range(r2):
                ball_list_1.append("R")
            for i in range(g2):
                ball_list_1.append("G")
            for i in range(b2):
                ball_list_1.append("B")
            ball_a_1, ball_b_1 = random.choices(ball_list_1, k=2)
            if ball_a_1 == "R":
                r2 -= 1
            elif ball_a_1 == "G":
                g2 -= 1
            elif ball_a_1 == "B":
                b2 -= 1
            if ball_b_1 == "R":
                r2 -= 1
            elif ball_b_1 == "G":
                g2 -= 1
            elif ball_b_1 == "B":
                b2 -= 1
            if ball_a_1 == ball_b_1:
                if ball_a_1 == "R":
                    r1 += 1
                elif ball_a_1 == "G":
                    g1 += 1
                elif ball_a_1 == "B":
                    b1 += 1
            elif ball_a_1 != ball_b_1:
                if ball_a_1 != ball_b_1 != "R":
                    r1 += 1
                elif ball_a_1 != ball_b_1 != "G":
                    g1 += 1
                elif ball_a_1 != ball_b_1 != "B":
                    b1 += 1
            turn -= 1
            if r1 + g1 + b1 == 1 and r2 + g2 + b2 == 0:
                if r1 == 1:
                    return "R"
                elif g1 == 1:
                    return "G"
                elif b1 == 1:
                    return "B"


r1, g1, b1, r2, g2, b2 = num_input()
print(game(r1, g1, b1, r2, g2, b2, 0))


