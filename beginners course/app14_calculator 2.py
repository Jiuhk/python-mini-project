snum1 = input("Enter your first number: ")
meth = input("+ or - or * or / : ")
snum2 = input("Enter your second number: ")
num1 = float(snum1)
num2 = float(snum2)

if meth == "+":
    print(num1 + num2)
elif meth == "-":
    print(num1 - num2)
elif meth == "*":
    print(num1 * num2)
elif meth == "/":
    print(num1 / num2)
else:
    print("please enter correctly.")
