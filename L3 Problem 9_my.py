#The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

print('Please think of a number between 0 and 100!')
min = 0
max = 100
ans = 0

while True:

  print('Is your secret number ' + str((max+min)/2) + '?')
  
  input = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
  if input == 'h':
    max = (max+min)/2
  elif input == 'l':
    min = (max+min)/2
  elif input == 'c':
    ans = (max+min)/2
    print('Game over. Your secret number was: ' + str(ans))
    break
  else:
    print('Sorry, I did not understand your input.')
