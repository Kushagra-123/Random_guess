import random
randnumber = random.randint(1,100)
print(randnumber)

userguess = None
guess  = 0
while(randnumber!=userguess):
    userguess = int(input("Enter your guess"))
    guess = guess +1
    if(userguess == randnumber):
        print("you guessed right")        
    else:
        if(userguess>randnumber):
            print("you guessed it wrong ,enter the smaller number")
        else:
            print("ou guessed it wrong ,enter the larger number")
        
print(f"You guessed the number in {guess} guesses")

with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if(guess<hiscore):
    print("you have broken thr high score!")
    with open("hiscore.txt","w") as f:
        f.write(str(guess))

    
    
