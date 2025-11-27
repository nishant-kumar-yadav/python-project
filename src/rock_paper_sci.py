import random 
print("WELCOME TO ROCK,PAPER & SCI")
name=input("enter your name -> ")
print(f"Welcome , {name.title()}")
def rock_paper_scissors():
    
    allowed_rock=["rock","r","1","ro","roc","rck","rk","rc"]
    allowed_paper=["paper","2","pa","p","pap","pape","papr","per"]
    allowed_scissors=["sci","scissors","s","3"]
    bot_score=0
    your_score=0
    while bot_score<3  and your_score<3:
        options=["rock","paper","scissors"] 
        bot_choice=random.choice(options)
        while True:
            a=input("enter your choice -> ").lower()
            if a in allowed_paper or a in allowed_rock or a in allowed_scissors:
                break
            else:
                print("enter a valid choice")
        if a in allowed_paper:
            a="paper"
        elif a in allowed_rock:
            a="rock"
        else:
            a="scissors"
        l=[a,bot_choice]
        if set(l)=={"paper"} or set(l)=={"rock"} or set(l)=={"scissors"} :
            print("my choice -> "f"{bot_choice}")
            print("opps! its a draw")
        elif set(l)=={"paper","rock"}:
            if l==["paper","rock"] :
                your_score+=1
                print("my choice -> "f"{bot_choice}")
                print("you won")
                print(f"score: {your_score}-{bot_score}")
            else:
                bot_score+=1 
                print("my choice -> "f"{bot_choice}")
                print("you lost")
                print(f"score: {your_score}-{bot_score}")
        elif set(l)=={"rock","scissors"}:
            if l==["rock","scissors"] :
                your_score+=1
                print("my choice -> "f"{bot_choice}")
                print("you won")
                print(f"score: {your_score}-{bot_score}")
            else:
                bot_score+=1 
                print("my choice -> "f"{bot_choice}")
                print("you lost")
                print(f"score: {your_score}-{bot_score}")
        else:
            if l==["scissors","paper"]:
                your_score+=1
                print("my choice -> "f"{bot_choice}")
                print("you won")
                print(f"score: {your_score}-{bot_score}")
            else:
                bot_score+=1 
                print("my choice -> "f"{bot_choice}")
                print("you lost")
                print(f"score: {your_score}-{bot_score}")                
    if bot_score>your_score:
        print("better luck next time")
    else:
        print("you are good")

rock_paper_scissors()
for_rematch=input("press any key to play again or c for exit -> ")
while for_rematch!="c":
    rock_paper_scissors()
    for_rematch=input("press any key to play again or c for exit -> ")
else:
    print("thanks for playing")

