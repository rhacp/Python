print("CHALLENGE 13")
print("---")
print()

price = int(input("Enter initial price: "))
discount = int(input("Enter discount value (%): "))
print()

rez = price - (price * discount / 100)
print(f"The final price is: {rez}")