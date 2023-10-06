name = "Andrei"
print(name)
print()
age = 39

print(type(name) == str)
print(isinstance(name, str))
print()

age = float(2)
print(isinstance(age, int))
print(isinstance(age, float))
print()

age2 = "20"
print(isinstance(age2, int))
age2 = int("20")
print(isinstance(age2, int))
print()

age3 = "20"
age4 = int(age3)
print(isinstance(age4, int))
print()

a = False
print("a = " + str(a))
print("Is `a` boolean? Answer: " + str(isinstance(a, bool)))
print()

print('hi' or 'hey')
print([] or 'hey')
print(False or False)
print(False or 5)
print([] or False)
print(False or [])