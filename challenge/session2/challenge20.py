print("CHALLENGE 21")
print("---")
print()

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print()

print("a") if a > c else print("c") if a > b else print ("b") if c < b else print("c")