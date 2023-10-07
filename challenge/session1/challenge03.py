print("CHALLENGE 3")
print("---")
print()

number = int(input("Enter your number: "))
help_variable = False
print()
print(f"Is your number positive?")
if number > 0:
    print(bool(~help_variable))
else:
    print(help_variable)
print()
# ~true = true
# ~false = ture

number = int(input("Enter second number: "))
help_variable_two = True
print()
print(f"Is your number positive?")
if number < 0:
    print(not help_variable_two)
else:
    print(help_variable_two)
# not true = false
# not false = true
