import tkinter as tk

import random
words = ["RANGE","TUPLE","FRUIT","MANGO","PRINT","PLACE","INPUT"]
x = 0
r = 0
called_letter=[]
print("Welcome to this tricky word guessing game.Here each word will be of 5 letters and a letter will only occur once in the word.So,please choose wisely.Have Fun!😉👌  ")
print("You have a total of 10 guesses. You Have to find 5 letters.Pretty tricky,right??Computer will choose a word from our dictionary.So if you have the dictionary,it'll be fun for you.")
print("The words are : ")
for word in words:
    print(word,end=" ")
print()
word = random.choice(words)
while x < 5 and r < 10:
    letter = input("Guess a letter in the secret word:(All in Uppercase,5 letter word) ").capitalize()
    if letter in word and letter not in called_letter:
        print(f"There is a {letter} in the word.")
        x = x + 1
        r = r + 1
        called_letter.append(letter)
        print(f"You Have {10 - r} guesses left")
        print(f"You Have found {x} out of 5 letters")
    elif letter in word and letter in called_letter:
        print(f"You Have already found {letter} in the word.No need to find it again.You lose one guess.")
        r=r+1
        print(f"You Have {10 - r} guesses left")
        print(f"You Have found {x} out of 5 letters")
    else:
        print(f"There is no {letter} in the word.")
        r = r + 1
        print(f"You Have {10 - r} guesses left")
        print(f"You Have found {x} out of 5 letters")
if x == 5:
    print("You Won!")
    print("The word was: " +word)
else:
    print("You Lose!")
    print("The word was: " + word)