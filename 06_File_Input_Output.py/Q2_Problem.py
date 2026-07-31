import random 

def game():
    print("You are Playing a game..")
    score= random.randint(1,100)
    #fetch highscore
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore =int(highscore)
        else:
            highscore =0
            
    print(f"Your score = {score}")
    if(score>highscore):
        #write this in your file or save it in your file.
        with open("highscore.txt","w") as f:
            f.write(str(score))
            
    return score

game()
