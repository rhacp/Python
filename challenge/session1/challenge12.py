print("CHALLENGE 12")
print("---")
print()

a = 10

print("Using for reversed:")
for number in reversed(range(1, 11)):
    print(number, end=" ")
print()
print()
print("Decrementing variable at each step:")
for number in range(1, 11):
    print(a, end=" ")
    a -= 1
