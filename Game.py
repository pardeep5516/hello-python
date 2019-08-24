import random
print("Welcome to ROCK, PAPER, SCISSOR Game")
random_number = random.randint(0, 2)
computer = " "
computer_score = 0
user_score = 0
if(random_number == 0):
    computer = "rock"
elif(random_number == 1):
    computer = "paper"
else:
    computer = "scissor"
found = True
while(found):
    user = input("rock or paper or scissor: ")
    if(computer == "rock" and user == "paper"):
        print("Winner is user........! ", user)
        print("computer choice is ", computer)
        user_score += 1
    elif(computer == "rock" and user == "scissor"):
        print("Winner is computer........! ", computer)
        print("user choice is ", user)
        computer_score += 1
    elif(computer == "paper" and user == "rock"):
        print("Winner is user........! ", user)
        print("computer choice is ", computer)
        user_score += 1
    elif(computer == "paper" and user == "scissor"):
        print("Winner is computer........! ", computer)
        print("user choice is ", user)
        computer_score += 1
    elif(computer == "scissor" and user == "rock"):
        print("winner is user........! ", user)
        print("computer choice is ", computer)
        user_score += 1
    elif(computer == "scissor" and user == "paper"):
        print("winner is computer.........! ", computer)
        print("user choice is ", user)
        computer_score += 1
    elif(computer == user):
        print("Tie")
        print("user choice is ", user, "and computer choice is ", computer)
    else:
        print("wrong entry try again")
    repeat = input("Do You want to play again(yes/no): ")
    if(repeat == "yes"):
        found = found
    elif (repeat == "no"):
        found = False
    else:
        print("wrong repeat")
if(user_score > computer_score):
    print("User score is Greater than Computer score")
    print("user total score is: ", user_score)
    print("compurer total score is: ", computer_score)
elif(user_score == computer_score):
    print("user and computer is same ")
    print("user total score is: ", user_score)
    print("computer total score is: ", computer_score)
else:
    print("computer score is Greater than user score ")
    print("user total score is: ", user_score)
    print("computer total score is: ", computer_score)
