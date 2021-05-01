# Handy Cricket

# Runs are in 1,2,3,4,5,6,10

# if same runs scored by both players then batsman will be OUT

# Player 1 Vs Computer

import random

player1 = input("Enter name of player 1 : ")
print('------------------------------------------------')
 
total = 0
ball = 0
boundaries = 0
fours = 0
sixes = 0


while True :
    runs = int(input('Enter runs scored by you : '))
    print("-------------------------------------------------------------")
    computer = random.randint(1, 6)
    ball = ball + 1
    if runs != 'esc':
        if runs < 0 :
            print('Runs cannot be negative')
            print("-------------------------------------------------------------")
        elif runs >= 7:
            print('These runs are not valid')
            print("-------------------------------------------------------------")
        elif runs == computer :
                print("Ouch ! You are OUT ," ,player1)
                print("Better Luck Next Time ! ")
                print(" >> Run The program again to play the game  << ")
                print("===================================================================") 
                break
                print("-------------------------------------------------------------") 
        elif runs == 1 or runs == 2 or runs == 3 or runs == 4 or runs == 5 or runs == 6 :
            total = total + runs
            print("Player Run =",runs)
            print("computer Runs = ",computer)
            print("===================================================================")
            if runs == 4 or runs == 6 :
                boundaries +=1
                if runs == 4 :
                    fours += 1
                if runs == 6 :
                    sixes += 1         
    else:
        break
    
print(player1)
print("===================================================================")
print("Total Runs = ", total)
print("Balls faced =",ball)
strike_rate = ( total / ball ) * 100
print("Strike Rate =",round(strike_rate,2))
print("boundaries scored =",boundaries)
print("fours =",fours)
print("sixes =",sixes)

    




    
