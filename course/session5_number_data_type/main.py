#NUMBER DATA TYPE

#INT = Integer
#FLOAT = Fraction, Number with decial
#COMPLEX = Complex Numer (Real Part+ Imaginary Part)

n1 = 2 + 3j
n2 = complex(2, 3)

print(n1.real, n2.imag)

print()
print("---")
#---
print()

#FUNCTIONS WITH NUMBERS

#ABS & ROUND

x = -5.5
y = -5.56

print(f"The absolut value of {x} is {abs(x)}")
print(f"The round value of {x} is {round(x)}")

print(f"The round value with one decimal of {y} is {round(y,1)}")
#Will round with once decimal

print()
print("---")
#---
print()

#ENUMS

from enum import Enum


class State(Enum):
  INACTIVE = 0
  ACTIVE = 1


print(State.ACTIVE)
