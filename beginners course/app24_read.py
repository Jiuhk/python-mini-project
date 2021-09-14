file = open("jjj", "r")

file_lines = file.readlines()
Lines = list(file_lines)
Lines.append("one")
print(Lines)
Lines = list(file_lines)
print(Lines)

file.close()
