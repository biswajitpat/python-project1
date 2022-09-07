# ROCK - PAPER - SCISSOR GAME
import random
from time import sleep 

def game(comp,you):
    #if all values are equal then declare a Tie
    if(comp==you):
        return None
    # Then Check for all Possibilities when coputer choose 
    elif(comp=='s'):
        if(you=='p'):
            return True
        elif(you=='c'):
            return False
    elif(comp=='p'):
        if (you=='s'):
            return False
        elif(you=='c'):
            return True
    elif(comp=='c'):
        if(you=='s'):
            return True
        elif(you=='p'):
            return False


print("\t\t\tWelcome To Your avourite Game: \t\t\t")
print("\t\t\t STONE@@ PAPER$$ SCISSOR##\t\t\t")

print("Computer's Turn : Stone(s) or Paper(p) or Scissor(c)?")
randnum= random.randint(1,3)
if (randnum==1):
    comp ='s'
elif (randnum==2):
    comp= 'p'
else:
    comp= 'c' 

print("Enter Your Choice:")
you= input(" Stone(s) or Paper(p) or Scissor(c)? --> ")
result= game(comp,you)
print("The Input of the Computer Was--> ",comp)
print("Your Input Was--> ",you)
if(result==None):
    print("It is A Tie")
elif(result== True):
    print("Hurrey!! Congratulations-- *******You WIN*******")
else:
    print("Sryy!! You Lose....... ")

