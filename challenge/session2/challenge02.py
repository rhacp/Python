print("CHALLENGE 2")
print("---")
print()

# Python is an object-oriented language, where every variable is an object/reference to an object.

a = 5
b = 5
print("a = 5")
print("b = 5")

'''
In Python, you'll have several built-in types at your disposal. Most of them are immutable, and a few are mutable. 
Single-item data types, such as integers, floats, complex numbers, and Booleans, are always immutable. 
So, you have no way to change the value of these types.

Objects of built-in type that are mutable are:

Lists
Sets
Dictionaries
User-Defined Classes (It purely depends upon the user to define the characteristics) 
Objects of built-in type that are immutable are:

Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
Strings
Tuples
Frozen Sets
User-Defined Classes (It purely depends upon the user to define the characteristics)
'''

#Any type of number variable is immutable
print()
print("a == b")
print (a == b) # True because they have the same value
print("a is b");
print (a is b) # True because int are immutables in Python, the same as with the StringPool in Java and they are reffering to the same Object

print()
b = 7
print("b = 7")
print()
print("a == b")
print (a == b)
print("a is b");
print (a is b)

#Lists are mutable
print()
list1 = [1, 3, 5]
list2 = [1, 3, 5]
print(f"list1: {list1}")
print(f"list2: {list2}")
print("list1 == list2")
print(list1 == list2)
print("list1 is list2")
print(list1 is list2) # False because they are immutable, so even if their values are equals, they do not refer to the same object in memory.
