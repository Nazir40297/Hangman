while True:
  guess = input("Guess a letter...\n")
  if len(guess) == 1 and guess.isalpha():
    break
  else:
    print("Invalid letter. Please, enter a single alphabetical character.")

word = "pineapple"  
  
if guess is in word:
  print(f"Good guess! {guess} is in the word.")
else:
  print(f"Sorry, {guess} is not in the word. Try again.")
