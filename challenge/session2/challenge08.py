print("CHALLENGE 8")
print("---")
print()

number = int(input("Enter your number: "))
factorial = 1;

for num in range(1, number + 1):
    factorial *= num;

print(f"{number}! = {factorial}")
