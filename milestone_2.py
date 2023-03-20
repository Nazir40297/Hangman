import random

word_list = ["pomegranate", "kiwi", "apple", "pineapple", "orange"]
word = random.choice(word_list)
print(word)
guess = input("Enter a single letter...\n")
if len(guess) == 1:
  print("Good guess!.")
else:
  print("Oops! That is not a valid input.")
