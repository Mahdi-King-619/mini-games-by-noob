import tkinter as tk
import random

player_score = 0
computer_score = 0
options = ("rock", "paper", "scissors")


def play(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(options)

    result_label.config(text=f"Computer chose {computer_choice}")
    if player_choice == computer_choice:
        outcome = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or (
            player_choice == "paper" and computer_choice == "rock") or (
            player_choice == "scissors" and computer_choice == "paper"):
        outcome = "You win this round!"
        player_score += 1
    else:
        outcome = "Computer wins this round!"
        computer_score += 1

    score_label.config(text=f"You:    {player_score}     |    Computer:   {computer_score}")
    outcome_label.config(text=outcome)

    if player_score == 10 or computer_score == 10:
        final = "🎉 You Win!" if player_score == 10 else "💻 Computer Wins!"
        outcome_label.config(text=final)
        rock_btn.config(state="disabled")
        paper_btn.config(state="disabled")
        scissors_btn.config(state="disabled")


root = tk.Tk()
root.title("Rock Paper Scissors")

score_label = tk.Label(root, text="You: 0  |  Computer: 0", font=("Arial", 14))
score_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

outcome_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 12))
outcome_label.pack()

rock_btn = tk.Button(root, text="Rock", width=15, command=lambda: play("rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper", width=15, command=lambda: play("paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(root, text="Scissors", width=15, command=lambda: play("scissors"))
scissors_btn.pack(pady=5)

root.mainloop()
