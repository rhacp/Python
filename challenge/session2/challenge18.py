print("CHALLENGE 18")
print("---")
print()

list_one = []
number_of_elements = int(input("Enter the number of elements: "))
for num in range(0, number_of_elements):
    list_one.append(num)
print()

print("Your list is: {", end="")
for num in range(0, number_of_elements):
    if num == number_of_elements - 1:
        print(f"{list_one[num]}}}", end="")
    else:
        print(f"{list_one[num]}, ", end="")
print()

for num in range(0, number_of_elements):
    list_one[num] -= 1

print("Your list is: {", end="")
for num in range(0, number_of_elements):
    if num == number_of_elements - 1:
        print(f"{list_one[num]}}}", end="")
    else:
        print(f"{list_one[num]}, ", end="")