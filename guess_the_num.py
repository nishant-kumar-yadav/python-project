import random
print("welcome to guessing game")
yourname= (input("enter your name : "))
name=yourname.title()

print( "hello ,",f"{name}")
def guess_the_num():
    
    count=0
    
    
    value=random.randint(0,99)
    print(value)
   


    while (count<5 ):
        flag=0
        num=int(input("guess a number: "  ))
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
            print("-> congratulation , you are correct")
            
            break
        if count==3:
            print("->last turn,")
        if count==4:
            print("-> you lose,",f"correct number was -> {value}")
            print("better luck next time.")
         
            
        count+=1
           
guess_the_num()
again=input("press YES for playing again, anything else for exit ->  ")

while again.lower()=="yes":
    guess_the_num()
    again=input("press YES for playing again, anything else for exit -> ")
else: 
    print("thanks for playing")



