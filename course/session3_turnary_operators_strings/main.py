#TURNARI OPERATOR


def is_adult(age):
  if age > 18:
    return True
  else:
    return False


def is_adult2(age):
  return True if age > 18 else False


#STRINGS

#"Beau"
#'Beau'

name = "Kors"
name += " is my name"

age = str(39)
name += f". I have {age} name"

print(name)
print()

#MULTIPLE LINE STRINGS

print("""Kors has
39
Gs of breeze""")

print()

# STRING METHODS

print("Kors".upper())
print("Kors".lower())
print("KoRs si dIor".title())
print("Kors".islower())
print()

name = "Kors"
print(name.lower())
print(name)
print()

print("Kors".isalpha())
#to check if a string contains only characters and is not empty

print("23".isalnum())
#to check if a string cotains characters or digits and is not empty

print("Kors".isdecimal())
#to check if a string contains only digits and is not empty
print()

print("Kors".startswith("Ko"))
#to check if the string starts with a specific substring

print("Kors".endswith("Ko"))
print()

print("Kors".replace("Ko", "U"))
#to replace a part of a string

print("Ko rs".split())
#to split a string into a list where each word is a list item
print()

incantation = ["In", "the", "name", "of", "God!"]
print(" ".join(incantation))
# The string join() method returns a string by joining all the elements of an iterable (list, string, tuple), separated by the given separator.
print()

#contor = str(input("Input the Contor: "))
#x = "Kors".find(contor)
##to find the position of a substring
#x += 1
#print(f"{contor} is on the position {x} in Kors.")
#print()

print(len(name))
#to find the lenght of a string
print()

print("l" in name)
#to find if a substring in part of a string (boolean)
print()

print("Ko\"rs")
#ca sa afisam ghilimele si alte caractere. \ ne spune ca urmatorul este doar simbol
print()

print("Ko\ars")
#\a ???
print()

#lean = 'Ko\rsfsefsae'
#print(lean)
#\ escapes a character usually
#print()

print("Ko\\rs")
#\\ ca sa afisam \
print()

print(name[0])
#to get the character from a specific position
print()

print(name[0:2])
#to get the character from a specific position
print()

print(name[:2])
#to get the character from a specific position
print()

print(name[1:])
#to get the character from a specific position
print()

#BOOLEAN OPERATORS
