#BOOLEAN OPERATORS

#done = True
#Boolean True and False are ALWAYS put with cappital letters, otherwise it will not be loaded as a boolean

done = input("Choose a boolean value: ")

if done == "False":
  done = bool(done)
  print(type(done))
elif done == "True":
  done = bool(done)
  print(type(done))
elif done.isdecimal():
  done = int(done)
  print(type(done))
elif done == "":
  done = str(done)
  print(type(done))
elif done.isalnum():
  done = str(done)
  print(type(done))

#BOOL COMPARISION TO NULL/FALSE (ALSO MADE FOR INTEGER OR STR)

#STR is False if it contains no character
#INT is False if it is equal to 0
#BOOL is False only if it is actually Flase

if done:
  print("Yes, it is true.")
else:
  print("No, it is false.")

print()
print("---")
#---
print()

#INT COMPARISION TO NULL

number = [0, 156]
if number[0]:
  print(str(number[0]) + " is Positive")
else:
  print(str(number[0]) + " is Negativ")

if number[1]:
  print(str(number[1]) + " is Positive")
else:
  print(str(number[1]) + " is Negativ")

print()
print("---")
#---
print()

#ANY & ALL

a = False
b = True
c = any([a, b])
print(c)

c = all([a, b])
print(c)

print()
print("---")
#---
print()
