import tkinter as tk

questions= ["Who is the current Head of the state of Bangladesh?: ",
            "What is the 2nd formula of newton?: ",
            "How many bones are there in Human Body?: ",
            "Which planet in the solar system is the hottest?: ",
            "What is the equation of a sphere in 3D system?: ",
            "Who is the singer of the song ""Without me""?: "]
options=[("A.Dr. Muhammad Yunus","B.Dr. Muhammad Yusuf","C.Dr.Muhammad Mahdi","D.Dj Snake"),
         ("A.F=ma","B.F=m*(dp/dt)","C.None of them","D.Both A & B"),
         ("A.206","B.207","C.208","D.209"),
         ("A.Venus","B.Neptune","C.Saturn","D.Earth"),
         ("A.x²+y²+z²=1","B.x³+y³+z³=27","C.x²-y³+z²=4","D.None Of these"),
         ("A.Beyonce","B.DJ Snake","C.Eminem","D.Bongoboltu"),]
answers=["A","D","A","A","A","C"]
guesses=[]
score=0
question_num=0
def option_choice(guess):
    global score,question_num
    outcome_label.config(text=questions[question_num])
    if guess==answers[question_num]:
        score+=1
        outcome = "Your guess is correct!"
    else:
        outcome = f"Incorrect!The answer was {answers[question_num]}"
    question_num+=1
    score_label.config(text=f"Your Score: {score}/{question_num}")
    outcome_label.config(text=outcome)


    if question_num == len(questions) and score>2:
        final="You Win!"
        outcome_label.config(text=final)
        A_btn.config(state="disabled")
        B_btn.config(state="disabled")
        C_btn.config(state="disabled")
        D_btn.config(state="disabled")
    elif question_num == len(questions) and score<3:
        final="You Lose!"
        outcome_label.config(text=final)
        A_btn.config(state="disabled")
        B_btn.config(state="disabled")
        C_btn.config(state="disabled")
        D_btn.config(state="disabled")
    else:
        load_questions()
def load_questions():
    question_label.config(text=questions[question_num])
    A_btn.config(text=options[question_num][0])
    B_btn.config(text=options[question_num][1])
    C_btn.config(text=options[question_num][2])
    D_btn.config(text=options[question_num][3])
root = tk.Tk()
root.title("Quiz Game")

score_label = tk.Label(root, text="Your Score: 0",font=("Arial",20))
score_label.pack()

question_label = tk.Label(root, text=f"Question Number: {question_num+1}" + questions[question_num],font=("Arial",20))
question_label.pack(pady=10, padx=10)
outcome_label = tk.Label(root, text="Choose A,B,C or D", font=("Arial", 20))
outcome_label.pack()

A_btn = tk.Button(root, text="".join(options[question_num][0]), width=30, command=lambda: option_choice("A"))
A_btn.pack(pady=5)

B_btn = tk.Button(root, text="".join(options[question_num][1]), width=30, command=lambda: option_choice("B"))
B_btn.pack(pady=5)

C_btn = tk.Button(root, text="".join(options[question_num][2]), width=30, command=lambda: option_choice("C"))
C_btn.pack(pady=5)

D_btn = tk.Button(root, text="".join(options[question_num][3]), width=30, command=lambda: option_choice("D"))
D_btn.pack(pady=5)
root.mainloop()


