import random
def help_msg():
    print("\n" + "="*40)
    print("       --- GAME RULES & HELP ---")
    print("="*40)
    print("1. THE GOAL: Guess the secret number between 0 and 99.")
    print("2. LIVES: You have exactly 5 attempts to win.")
    print("-" * 40)
    print("3. HINTS (How to read them):")
    print("   * 'In the clouds / Rock bottom' -> You are far off (20+ away).")
    print("   * 'Too high / Too low'          -> You are getting closer.")
    print("   * 'Very close / Almost there'   -> You are within 5 numbers!")
    print("-" * 40)
    print("4. SCORING SYSTEM:")
    print("   * 1st Try: 100 pts   * 4th Try: 20 pts")
    print("   * 2nd Try: 50 pts    * 5th Try: 10 pts")
    print("   * 3rd Try: 30 pts    * Lose:    0 pts")
    print("="*40 + "\n")
print("welcome to guessing game")
yourname= (input("enter your name : "))

name=yourname.title()
l=[]
cround=len(l)


print( "hello ,",f"{name}")
help_msg()
def guess_the_num():
    
    count=1
    
    
    
    value=random.randint(0,99)
    
   

    score=0
    while (count<6 ):
        try:
            num = int(input("guess a number: "))
        except ValueError:
            print("-> That is not a number! Please enter digits only.")
            continue
        if num not in range(0,100):
            print('-> enter num between 0 to 99 ')
            
            continue
            
        if num!=value:
            if num>value:
                if (num-value)>=20:
                    print("-> You're in the clouds! Try a much smaller number")
                elif (num-value)<=5:
                   print("-> You are very close, but try a bit lower.")    
                else:
                   print("-> too high")
            if value>num:
                if (value-num)>=20:
                    print("-> Rock bottom! You need a much bigger number")
                elif (value-num)<=5:
                    print("-> Almost there! Just higher") 
                else:
                    print("-> too low")               
        else:
            if count==1:
                score+=100
            elif count==2:
                score+=50
            elif count==3 :
                score+=30
            elif count==4:
                score+=20
            elif count==5:
                score+=10
            l.append(score)        


            print("-> congratulation , you are correct...  your score = "f"{score}")

            
            
            break
        if count==4:
            print("->last turn,")
        if count==5:
            print("-> you lose,",f"correct number was -> {value}")
            l.append(0)
            print("better luck next time.")


         
            
        count+=1
        
           
guess_the_num()




again=input("press any for playing again, C for exit ->  ")

while again.lower()!="c":
    cround=len(l)
    print(f"round {cround+1} start")
    
    guess_the_num()
    
    again=input("press any for playing again, C for exit -> ")
    
else: 
    print("thanks for playing")
    totalscore=sum(l)
    print("total score -> "f"{totalscore} in {len(l)} round")



