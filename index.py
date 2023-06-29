def checkInput(inputGiven):
    if(inputGiven==1):
        return "ROCK"
    elif(inputGiven==2):
        return "SCISSORS"
    else:
        return "PAPER"
    

import random


print("Welcome To The Game") 
print("Rock Paper Scissors") 
print()
char = input("Would you like to start the game(Y/N): ")
print()
if(char=="Y"):
    print("Let's start the game without any delay") 
    print()
    no_of_round = 1
    computer_wins = 0 
    user_wins = 0
    while(True):
        
        print("ROUND NUMBER : "+str(no_of_round))
        print()
        print("1.ROCK") 
        print("2.SCISSORS") 
        print("3.PAPER")
        print()
        user_input = int(input("Chose Your Element(1-3): "))
        computer_input = random.randint(1,3); 
        print()
        if(not (user_input>=1 and user_input<=3)):
            print("Invalid Choice . . . Please give valid input") 
            continue
        
        print("Your input is     :"+ checkInput(user_input))
        print("Computer input is :"+ checkInput(computer_input))
        
        print()
        if(user_input==computer_input):
            print("Draw match")
        else:
            if(user_input==1):  
                if(computer_input==2):
                    print("USER WINS")
                    user_wins+=1
                else:
                    print("COMPUTER WINS")
                    computer_wins+=1
            elif(user_input==2):
                if(computer_input==1):
                    print("COMPUTER WINS") 
                    computer_wins+=1
                else:
                    print("USER WINS")
                    user_wins+=1
            else:
                if(computer_input==1):
                    print("USER WINS") 
                    user_wins+=1
                else:
                    print("COMPUTER WINS")
                    computer_wins+=1
        print()
        print("Computer has won "+str(computer_wins)+" games")
        print("User     has won "+str(user_wins)+" games")
        print()
        continouson = input("Do you want to continue(Y/N): ")
        if(continouson=="Y"):
            no_of_round+=1
            continue;
        else:
            break;
        


print("Thank You! Have a Nice day . . .")



    

