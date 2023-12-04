usrGuessNumLettersInAlphabet = 0

LETTERS_IN_ALPHABET = 26

usrGuessNumLetttersInAlphabet = int(input("How many letters are in the alphabet: "))

if usrGuessNumLetttersInAlphabet == LETTERS_IN_ALPHABET:
  print("correct")
else:
  print("incorrect")