def translate(phrase):
    result = ""
    for letter in phrase:
        if letter.lower() in "eiou":
            if letter.islower():
                result += "a"
            else:
                result += "A"
        else:
            result += letter
    return result


loop = True
while loop:
    x = input("Enter a phrase(enter N to end): ")
    if x == "N":
        print("End of translation.")
        loop = False
    else:
        print(translate(x))
