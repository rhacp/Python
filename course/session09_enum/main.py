#ENUMS

from enum import Enum


class State(Enum):
  INACTIVE = 0
  ACTIVE = 1


print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])

print()
print("---")
print()

print(list(State))
print(len(State))

print()
print("---")
#---
