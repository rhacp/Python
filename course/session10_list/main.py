#LISTS

dogs = ["2PAC", 1, "Biggie", True]
myhearth = []

print("AKA47" in dogs)
print("AKA47" in myhearth)

print()

dogs[1] = "Eminem"
print(f"The list is: {dogs}")
print(f"The third element is: {dogs[2]}")

print()

print(dogs[-1])
print(f"Elemente de la 2 la 4: {dogs[1:4]}")
print(f"Elemente pana la 3: {dogs[:3]}")
print(f"Number of elements of list: {len(dogs)}")

print()

dogs.append(input("Adauga element nou: "))
print(f"The list is: {dogs}")
print(f"Number of elements of list: {len(dogs)}")

print()

dogs.extend(["DrDre", "MamaTa"])
print(f"The list is: {dogs}")
print(f"Number of elements of list: {len(dogs)}")

print()

dogs += ["Akon"]
print(f"The list is: {dogs}")
print(f"Number of elements of list: {len(dogs)}")

print()

dogs += "Akon"
print(f"The list is: {dogs}")
print(f"Number of elements of list: {len(dogs)}")

print()

dogs.remove(True)
print(f"The list is: {dogs}")
print(f"Number of elements of list: {len(dogs)}")

print()

print(f"The element we will remove: {dogs.pop()}")
print(f"The list is: {dogs}")
print(f"Number of elements of list: {len(dogs)}")

print()

print(f"We will eliminate the element on the third position: {dogs.pop(2)}")
print(f"The list is: {dogs}")
print(f"Number of elements of list: {len(dogs)}")

print()

test = input("Element you want to add on the third position: ")
dogs.insert(2, test)
print(f"The list is: {dogs}")
print(f"Number of elements of list: {len(dogs)}")

print()

#dogs[1:1] = ["Test1", "Test2"]
#print(f"The list is: {dogs}")
#print(f"Number of elements of list: {len(dogs)}")

print()

dogs[1:2] = ["Test1", "Test2"]
print(f"The list is: {dogs}")
print(f"Number of elements of list: {len(dogs)}")

print()

dogs[2:4] = ["Test1A", "Test2A", "Test3A"]
print(f"The list is: {dogs}")
print(f"Number of elements of list: {len(dogs)}")

print()

dogs.sort()
print(f"The list is: {dogs}")
print(f"Number of elements of list: {len(dogs)}")

print()

dogs.sort(key=str.lower)
print(f"The list is: {dogs}")
print(f"Number of elements of list: {len(dogs)}")

print()

dogscopy = dogs[:]
print(f"Copie: {dogscopy}")
