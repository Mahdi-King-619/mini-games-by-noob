#Python Quiz Game

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

answers=["A","D","A","A","B","C"]

guesses=[]

score=0

question_num=0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Guess a option as the correct answer: ")
    guesses.append(guess)
    if guess.capitalize()==answers[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"the correct answer is {answers[question_num]}")
    question_num+=1
print("answers: ",answers)
print("guesses: ",guesses)
print(f"You answered {score} out of {len(questions)} questions.")
