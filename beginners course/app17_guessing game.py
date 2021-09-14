ans = "jupiter"
guess = ""
guess_num = 0
guess_lim = 3
guess_rem = guess_lim - guess_num
out_of_guesses = False


while guess != ans and not out_of_guesses:
    if guess_num < guess_lim:
        guess = input("Make a guess: ")
        guess_num += 1
        print("you have " + str(guess_lim - guess_num) + " guesses left.")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("you lose")
else:
    print("you win")