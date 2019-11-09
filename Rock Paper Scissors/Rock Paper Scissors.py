
# 1 = R ; 2 = P ; 3 = S
print ("This is a a game of Rock Paper and Scissors")

import random
move = [1, 2, 3]

def game():
    print("R for Rock; P for Paper; S for Scissors" + "\n")
    scply = 0
    sccom = 0
    round = 0
    n = True
    while n == True:
        print ("Round played: " + str(round))
        print("Score = " + str(scply) + " : " + str(sccom) + "  (Player/Computer)" + "\n")
        com = move[random.randint(0, 2)]
        ply = input("Your move: \n")
        if ply == "R":
            if com == 1:
                print("Computer's move: Rock")
                print("Tie")
            elif com == 2:
                print("Computer's move: Paper")
                print ("Lose")
                sccom = sccom + 1
            elif com == 3:
                print("Computer's move: Scissors")
                print ("Win")
                scply = scply +1
            print( "-----------------------" )
        elif ply == "P":
            if com == 2:
                print("Computer's move: Paper")
                print("Tie")
            elif com == 1:
                print("Computer's move: Rock")
                print ("Win")
                scply = scply + 1
            elif com == 3:
                print("Computer's move: Scissors")
                print ("Lose")
                sccom = sccom +1
            print( "-----------------------" )
        elif ply == "S":
            if com == 3:
                print("Computer's move: Scissors")
                print("Tie")
            elif com == 1:
                print("Computer's move: Rock")
                print ("Lose")
                sccom = sccom +1
            elif com == 2:
                print("Computer's move: Paper")
                print ("Win")
                scply = scply + 1
            print( "-----------------------")
        else:
            print ("Invalid input, try again.")
            print("-----------------------")
            round = round - 1
        round = round + 1
game()