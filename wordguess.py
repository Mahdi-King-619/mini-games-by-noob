import tkinter as tk
import random

words = [
    "RANGE","TUPLE","FRUIT","MANGO","PRINT","PLACE","INPUT",
    "CRANE","STORM","FLUID","CHARM","BLAST","QUOTE","VEXIL",
    "CROWN","SHAPE","GRIND","HONEY","QUICK","FOAMY","BRICK",
    "LIGHT","JUMPY","SWORD","CHEST","BRAVE","FIGHT","CLOUT",
    "INDEX","ZEBRA","KNIFE","GHOST","CHIRP","BOUND","CRAFT",
    "MUSIC","NOVEL","PIANO","CHALK","STING","GLARE","SWIFT",
    "DREAM","LUNCH","TRICK","SMILE","WOUND","PULSE","TRACK",
    "CLOUD","FRAME","SHOCK","BLEND","WHISK","TANGO","MARCH",
    "DRIVE","SCOUT","QUEST","LOVER","PAINT","WHEAT","CHIEF"
]

word = random.choice(words)


x = 0
r = 0
called_letter = []
progress = ["_"] * 5

def guess_letter():
    global x, r
    letter = entry.get().upper()
    entry.delete(0, tk.END)

    if not letter or len(letter) != 1:
        status_label.config(text="Enter ONE letter!")
        return

    if r >= 12 or x >= 5:
        return

    if letter in word and letter not in called_letter:
        status_label.config(text=f"There is a {letter} in the word.")
        called_letter.append(letter)
        r += 1
        for i, ch in enumerate(word):
            if ch == letter:
                progress[i] = letter
                x += 1
    elif letter in word and letter in called_letter:
        status_label.config(text=f"You already guessed {letter}. Guess wasted.")
        r += 1
    else:
        status_label.config(text=f"There is no {letter} in the word.")
        r += 1

    progress_label.config(text=" ".join(progress))
    guesses_label.config(text=f"Guesses left: {12 - r}")
    found_label.config(text=f"Letters found: {x}/5")

    if x == 5:
        status_label.config(text="🎉 You Won! The word was " + word)
        guess_btn.config(state="disabled")
    elif r >= 12:
        status_label.config(text="😢 You Lose! The word was " + word)
        guess_btn.config(state="disabled")

root = tk.Tk()
root.title("Word Guessing Game")

intro_text = (
    "Welcome to this tricky word guessing game.\n"
    "Each word will be 5 letters and each letter only occurs once.\n"
    "You have 10 guesses to find all 5 letters. Pretty tricky, right?\n"
    "The computer has chosen a word from our dictionary below.\n\n"
    "Words: " + ", ".join(words)
)

intro_label = tk.Label(root, text=intro_text, wraplength=400, justify="left", fg="darkblue")
intro_label.pack(pady=10)

progress_label = tk.Label(root, text=" ".join(progress), font=("Arial", 20))
progress_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=5, justify="center")
entry.pack()
entry.focus()

guess_btn = tk.Button(root, text="Guess", command=guess_letter)
guess_btn.pack(pady=5)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

guesses_label = tk.Label(root, text="Guesses left: 10")
guesses_label.pack()

found_label = tk.Label(root, text="Letters found: 0/5")
found_label.pack()

root.mainloop()
