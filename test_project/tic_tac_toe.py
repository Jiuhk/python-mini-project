import random
from slot import slot

a1 = slot("a1", "-")
a2 = slot("a2", "-")
a3 = slot("a3", "-")
b1 = slot("b1", "-")
b2 = slot("b2", "-")
b3 = slot("b3", "-")
c1 = slot("c1", "-")
c2 = slot("c2", "-")
c3 = slot("c3", "-")
free_slots = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
win = False
lose = False

print("********************************")
print("Welcome to the tic-tac-toe game!")
print("********************************")
name = input("Enter your name: ")
print("\nGood luck beating the computer, stupid " + name + "!")

start = ""
while start != "y":
    start = input("\nEnter y to start the game: ")


while not win and not lose and len(free_slots) != 0:

    print("\n  1", "2", "3")
    print("a", a1.value, a2.value, a3.value)
    print("b", b1.value, b2.value, b3.value)
    print("c", c1.value, c2.value, c3.value)
    print("")
    move = input("Enter your move(e.g. a1, b2...etc): ")

    for slot in free_slots:
        if slot.name == move:
            slot.value = "o"
            free_slots.remove(slot)

            if a1.value == a2.value == a3.value == "o" or b1.value == b2.value == b3.value == "o" or \
                    c1.value == c2.value == c3.value == "o" or a1.value == b1.value == c1.value == "o" or \
                    a2.value == b2.value == c2.value == "o" or a3.value == b3.value == c3.value == "o" or \
                    a1.value == b2.value == c3.value == "o" or a3.value == b2.value == c1.value == "o":
                win = True

            if not win and len(free_slots) != 0:
                cpu_move = random.choice(free_slots)
                cpu_move.value = "x"
                free_slots.remove(cpu_move)

                if a1.value == a2.value == a3.value == "x" or b1.value == b2.value == b3.value == "x" or \
                        c1.value == c2.value == c3.value == "x" or a1.value == b1.value == c1.value == "x" or \
                        a2.value == b2.value == c2.value == "x" or a3.value == b3.value == c3.value == "x" or \
                        a1.value == b2.value == c3.value == "x" or a3.value == b2.value == c1.value == "x":
                    lose = True


print("\n  1", "2", "3")
print("a", a1.value, a2.value, a3.value)
print("b", b1.value, b2.value, b3.value)
print("c", c1.value, c2.value, c3.value)
print("")

if win:
    print("Unbelievable, stupid " + name + "! You win!")
elif lose:
    print("Not surprised, stupid " + name + "! You lose!")
else:
    print("Tie!")
