print("CHALLENGE 4")
print("---")
print()

height_one = int(input("Enter first height: "))
height_two = int(input("Enter second height: "))
print()

maximum_height = 0 if height_one == height_two else height_one if height_one >= height_two else height_two
print(f"The higher value is: {maximum_height}") if maximum_height != 0 else print("The values are equals.")