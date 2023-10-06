#DICTIONARIES

dog = {"name": "PopSmoke", "age": 21, "death": "Gunshot"}
print(dog)
print(dog["name"])
dogcopy = dog.copy()

print()

dog["name"] = "SmokePop"
print(dog)

print()

print(dog.get("death"))
print(dog.get("color"))
print(dog.get("color", "Doesn't Exist!"))

print()

#print(dog.pop("name"))
#print(dog)

#print()

#print(dog.popitem())
#print(dog)

#print()

print("death" in dog)
print(dog.keys())
print(list(dog.keys()))
print(dog.values())
print(list(dog.values()))

print()

print(list(dog.items()))
print(len(dog))

print()

dog["valoare cash"] = "infinity"
print(dog)

print()

del dog["age"]
print(dog)

print("\n Copia doctionarului initial:")
print(dogcopy)
