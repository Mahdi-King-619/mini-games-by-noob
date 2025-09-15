import random

player_point = 0
Computer_point = 0
#Don't Stop, Make it pop
#DJ blow my speakers up
#Tonight, I'm gonna Fight
#Till we see the sunlight
#TiK ToK on the clock
#But the party don't stop , no.
while player_point < 10 and Computer_point < 10:
    player = input("Enter your choice:(rock,paper,scissors) ").lower()
    options = ("rock", "paper", "scissors")
    computer = random.choice(options)
    if player == "rock":
        if computer == "scissors":
            print("Computer chose:", computer)
            print("You chose:", player)
            print("You got a point.")
            player_point += 1
            print(f"Your point = {player_point}")
            print(f"Computer's point = {Computer_point}")
        elif computer == "paper":
            print("Computer chose:", computer)
            print("You Chose:", player)
            print("Computer got a point.")
            Computer_point += 1
            print(f"Your point = {player_point}")
            print(f"Computer's point = {Computer_point}")
        else:
            print("Computer chose:", computer)
            print("You Chose:", player)
            print("No point to anyone")
            print(f"Your point = {player_point}")
            print(f"Computer's point = {Computer_point}")
    elif player == "paper":
        if computer == "rock":
            print("Computer chose:", computer)
            print("You Chose:", player)
            print("You got a point.")
            player_point += 1
            print(f"Your point = {player_point}")
            print(f"Computer's point = {Computer_point}")
        elif computer == "scissors":
            print("Computer chose:", computer)
            print("You Chose:", player)
            print("Computer got a point.")
            Computer_point += 1
            print(f"Your point = {player_point}")
            print(f"Computer's point = {Computer_point}")
        else:
            print("Computer chose:", computer)
            print("You Chose:", player)
            print("No point to anyone")
            print(f"Your point = {player_point}")
            print(f"Computer's point = {Computer_point}")
    elif player == "scissors":
        if computer == "paper":
            print("Computer chose:", computer)
            print("You Chose:", player)
            print("You got a point.")
            player_point += 1
            print(f"Your point = {player_point}")
            print(f"Computer's point = {Computer_point}")
        elif computer == "rock":
            print("Computer chose:", computer)
            print("You Chose:", player)
            print("Computer got a point.")
            Computer_point += 1
            print(f"Your point = {player_point}")
            print(f"Computer's point = {Computer_point}")
        else:
            print("Computer chose:", computer)
            print("You Chose:", player)
            print("No point to anyone")
            print(f"Your point = {player_point}")
            print(f"Computer's point = {Computer_point}")
    else:
        print("Invalid Choice")
        print("Please enter your choice:(rock,paper,scissors) ")

if player_point == 10 or Computer_point == 10:
    if player_point == 10:
        print("You Win!")
    else:
        print("Computer Wins!")
