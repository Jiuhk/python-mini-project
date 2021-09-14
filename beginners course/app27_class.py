from Jobs import Jobs

copywriter = Jobs("entry", 21000, False)
writer = Jobs("Top", 10000, True)
hacker = Jobs("Top", 100000, True)

salary = [writer.salary, copywriter.salary, hacker.salary]

Jobs_list = [copywriter, writer, hacker]

print(max(salary))
print(Jobs_list)
print(copywriter)
