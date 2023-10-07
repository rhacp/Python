print("CHALLENGE 4")
print("---")
print()

print("On new line:")
for num in range(1, 11):
    print(num)

print()
print("On the same line:")
for num in range(1, 11):
    print(num, end=" ")

print()
print()
print("LIST")
print(list(range(1, 11)))

print()
print("Even from 10 to 20 on new line:")
for num in range(10, 20, 2):
    print(num)

print()
print("Even from 10 to 20 on the same line:")
variable = ""
for num in range(10, 20, 2):
    variable += str(num) + ", "
print(variable[:-2])
