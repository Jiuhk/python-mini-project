try:
    print(int(input("enter a number: ")))
except ValueError as a:
    print("error: " + str(a))