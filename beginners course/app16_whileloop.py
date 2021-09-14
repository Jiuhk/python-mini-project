output = []
n = (11, 13, 3, 4, 5, 6)
place = 0
if n[place] >= 10:
    output.append(n[place])
    print(output)
    place += 1
    output.append(n[place])
    print(output)
    print(len(n))


def bigger10(x, y, z, a, b, c):
    output = []
    n = [x, y, z, a, b, c]
    place = 0
    while place <= len(n):
        if n[place] >= 10:
            output.append(1)
            place += 1
    return output


print(bigger10(11, 12, 3, 4, 5, 6))

i = 1
while i <= 9:
    print(i)
    i += 1

print("Program ends.")

output = []
n = [11, 12, 3, 4, 5, 6]
place = 0
while place <= len(n):
    if n[place] >= 10:
        output.append(n[place])
        place += 1

print(output)
