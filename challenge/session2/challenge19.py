print("CHALLENGE 19")
print("---")
print()

age = int(input("Enter your age: "))
print()

if age < 0:
    print("Silly, your age cannot be negative.")
elif age >= 65:
    print("Senior.")
elif age >= 18:
    print("Adult.")
elif age >= 12:
    print("Teenager.")
else:
    print("Child.")
