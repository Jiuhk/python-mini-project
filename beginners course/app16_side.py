
def bigger10(x, y, z, q, w, e, r, t):
    output = []
    n = [x, y, z, q, w, e, r, t]
    i = 0
    while i <= len(n) - 1:
        if n[i] >= 10:
            output.append(n[i])
            i += 1
        else:
            i += 1
    return(output)


print(bigger10(11, 12, 3, 92, 23, 1, 23, 4))
