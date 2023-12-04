import random

usrGuess = 0
randomNum = 0


usrGuess = int(input("Guess a number between 1 and 10: "))
randomNum = random.randint(1, 3)


if usrGuess == randomNum:
  print("Correct")
else:
  print("Not what I was thinking")