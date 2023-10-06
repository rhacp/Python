import random


def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}.")
  print()

  if player == computer:
    return "It's a tie!"

  elif player == "rock":
    if computer == "scissors":
      return "You win!"
    else:
      return "You lose!"

  elif player == "paper":
    if computer == "rock":
      return "You win!"
    else:
      return "You lose!"

  elif player == "scissors":
    if computer == "paper":
      return "You win!"
    else:
      return "You lose!"

  return [player, computer]


choices = get_choices()
print(check_win(choices["player"], choices["computer"]))

#---

#USED

#and computer == "scissors":
#    return "You win!"
#  elif player == "rock" and computer == "paper":
#    return "You lose!"

#print(check_win("scissors", "paper"))
#print(result)

#choices = get_choices()
#print(choices)

#---

#FUNCTIONS
#def greeting():
#  return "Hi"

#PRINT
#response = greeting()
#print(response)

#INPUT
#a = input("Enter a choice (b, c, d): ")

#F-STRING
#age = 25
#print(f"Jim is {age} years old.")

#---

#DICTIONARIES
#dict = {"name": "beau", "color": "blue"}

#choices = {"player": player_choice, "computer": computer_choice}
#p_choices = choices["player"]

#---

#LISTS & RANDOM
#include random

#food = ["pizza", "carrots", "eggs"]
#dinner = random.choice(food)
#print(dinner)

#---

#IF
#a = 3
#b = 5
#if a > b:
#  print("yes")

#ELSE & ELIF
#age = 8
#if age >= 18:
#  print("You can drive.")
#elif age >= 16:
#  print("You can drive just scooters.")
#elif age >= 12:
#  print("You can use just an electric bicycle.")
#else:
#  print("You can't drive anything kid.")

#---
