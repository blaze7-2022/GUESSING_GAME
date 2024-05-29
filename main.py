import random
import os
import sys
import time
points1 = 0
points2 = 0
def game():
  global points1
  global points2
  while True:
  
   print("Welcome to the guessing game")
   print("Press 1 to begin")
   print("Press 2 to exit")
   userinput1 = int(input("player1>: "))
   userinput2  = int(input("player2<: "))
   if userinput1 == 1 and userinput2 == 1:
    print("Left or right")
    userinput3 = str(input("player1>: "))
    userinput4 = str(input("player2<: "))  
    if userinput3 == "left" and userinput4 == "left":
      print("Both of you don't get a point")
    elif userinput3 == "left" and userinput4 == "right":
      print("Player 2 gains a point")
      points2 += 1
    elif userinput3 == "right" and userinput4 == "left":
      print("Player 1 gains a point")
      points1 += 1
    elif userinput3 == "right" and userinput4 == "right":
      print("BONUS 3 POINTS FOR BOTH PLAYERS")
      points1 += 3
      points2 += 3
    else:
      print("Invalid input")
    os.system("clear")
    time.sleep(2)

    print("ROUND 2")
    print("Guess a number between 1 and 10 ") 
    userinput5 = int(input(">: "))
    userinput6 = int(input("<: "))
    number = random.randint(1,10)
    if userinput5 == number and userinput6 != number :
      print("GOLDEN BUZZER!!! PLAYER 1 GAINS 5 POINTS")
      points1 += 5
      break
    elif userinput5 == number and userinput6 == number:
      print("both players get a point")
      points1 += 1
      points2 += 1
      break
    elif userinput5 != number and userinput6 == number:
      print("GOLDEN BUZZER!!! PLAYER 2 GAINS 5 POINTS")
      points2 += 5
      break
    else:
      print("Both players don't gain a point")
      break
  print("PLAYER 1:", points1)
  print("PLAYER 2:", points2)
  if points1 > points2:
   print("PLAYER 1 WINS")
  elif points1 < points2:
   print("PLAYER 2 Wins")
  else:
   print("IT'S A DRAW!")
  
game()

