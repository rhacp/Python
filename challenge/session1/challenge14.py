print("CHALLENGE 14")
print("---")
print()

number = int(input("Enter your number: "))
min = int(input("Enter range min: "))
max = int(input("Enter range max: "))
print()

if number < max and number > min:
    print("The number is withing the specified range.")
else:
    print("The number is not within the specified range.")