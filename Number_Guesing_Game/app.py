import random
import time
number = random.randint(1,200)
name = input 

def intro():
  print("May I ask you for your name!..")
  name=input()
  print(name+" we are going to play a game . I am thinking of a number between 1 and 200")
  time.sleep(0.5)
  print("go head Guess!..")
  
  
def pick():
  guessesTaken = 0
  while guessesTaken<7:
    time.sleep(0.25)
    enter = input ("Guess:")
    try:
      guess = int(enter)
      if guess<=200 and guess>=1: 
                guessesTaken=guessesTaken+1
                if guessesTaken<7:
                  if guess<number:
                    print("the guess of the number is that you have entered is too low")
                  if guess>number:
                    print("the guess of number that you  have entered  is to high")
                  if guess!=number:
                    time.sleep(0.5)
                    print("Try Again !")
                if guess==number:
                  break
      if guess>200 or guess<1:
        print("silly Goose ! that number is'nt in the range")
        time.sleep(0.25)
        print("please enter a number between 1 and 200")
    except:
      print("i don't think that " +enter+"is a number .sorry")
  if guess==number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')
  if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))
        
playAgain="yes"
while playAgain=="yes" or playAgain=="y" or playAgain=="Yes" or playAgain=="YES":
    intro()
    pick()
    print("Do you want to play again?")
    playAgain=input()
        
                  
                    
                
        