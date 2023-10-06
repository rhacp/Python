#SETS

names = {"Andrei", "Mihai", "Andrei"}
print(f"Primul set este: {names}")
names2 = {"Andrei"}
print(f"Al doilea set este: {names2}")
names3 = {"Cristi"}
print(f"Al treilea set este: {names3}")

print()

print(f"Intersectia primelor doua seturi: \n {names & names2}")

print()

print(f"The union of the sets 1 and 3 is: \n {names | names3}")
print(f"The union of the sets 3 and 1 is: \n {names3 | names}")

print()

print(f"Diferenta dintre sirurile 1 si 2 este: \n {names - names2}")
print(f"Diferenta dintre sirurile 2 si 1 este: \n {names2 - names}")

print()

print(f"Is names2 a subset of names? \n {names > names2}")
print(f"Is names a superset of names2? \n {names2 < names}")

print()

print(len(names))
print(list(names))
print("Andrei" in names)