print("CHALLENGE 10")
print("---")
print()

list_one = []

list_one.append(input("Enter first list element: "))
list_one.append(input("Enter second list element: "))
print()

print(f"Your list: {list_one}")
print()

list_two = list_one.copy();
list_one.append(input("Enter third list element: "))
print()

print(f"Your new list: {list_one}")
print(f"Your old list: {list_two}")
