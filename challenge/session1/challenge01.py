print("CHALLENGE 1")
print("---")
print()

##a = int(input("Enter first name: "))
##b = int(input("Enter second name: "))
a = input("Enter second name: ")
b = input("Enter second name: ")

dif = int(a) - int(b);

print(f"The sum of the numbers is: {int(a) + int(b)}")
print(f"The difference of the numbers is: {dif}")
print(f"The product of the numbers is: {int(a) * int(b)}")

if (a >= b):
    print(f"The bigger number divided by the smaller one: is: {int(a) / int(b)}")
else:
    print(f"The bigger number divided by the smaller one is: {int(b) / int(a)}")
