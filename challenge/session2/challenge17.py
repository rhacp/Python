print("CHALLENGE 17")
print("---")
print()

help2 = input("Is username (boolean; True or False): ")
if help2 == "False":
    has_username = False
elif help2 == "True":
    has_username = True
print()
help = input("Is password (boolean; True or False): ")
if help == "False":
    has_password = False
elif help == "True":
    has_password = True
print()

if has_password == True and has_username == True:
    print("Authentication successful.")
elif has_password == False and has_username == True:
    print("Password is incorrect.")
elif has_password == True and has_username == False:
    print("Username incorrect.")
else:
    print("Authentication failed.")
