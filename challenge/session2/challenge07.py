print("CHALLENGE 7")
print("---")
print()

side_one = int(input("Enter the first side: "))
side_two = int(input("Enter the second side: "))
side_three = int(input("Enter the third side: "))
print()

help_counter = 0 if side_one == side_two and side_two == side_three else 1 if side_one == side_two or side_two == side_three or side_three == side_one else 2

match help_counter:
    case 0:
        print("Equilateral")
    case 1:
        print("Isosceles")
    case 2:
        print("Scalene")