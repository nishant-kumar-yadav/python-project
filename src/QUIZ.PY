import random
import math 
import time 
q=open("ques.txt" ,"r")
ques_ans_dict=dict()
for i in range (0,49):
    data=q.readline()
    clear_data=data.split(":")
    one_q_a_dict={clear_data[0]:clear_data[1].strip()}
    ques_ans_dict.update(one_q_a_dict)

    
ques_list=list(ques_ans_dict.keys())
def display_quiz_rules(total_questions: int):
    """
    Displays the scoring rules, time tiers, and bonus thresholds 
    to the player in a professional, readable format.
    
    Args:
        total_questions (int): The number of questions in the current quiz
                               (used to calculate specific bonus time limits).
    """
    
    # Calculate bonus thresholds in minutes and seconds for clarity
    gold_bonus_min = total_questions / 3
    silver_bonus_min = total_questions / 2
    
    # Convert to M:S format for display
    def format_time(minutes):
        mins = int(minutes)
        secs = int((minutes - mins) * 60)
        return f"{mins}m {secs}s"

    print("\n" + "="*60)
    print(f"{'QUIZ SCORING PROTOCOL':^60}")
    print("="*60)
    
    print(f"\n[{'BASE SCORING SYSTEM':^25}]")
    print("-" * 60)
    print(f"{'Time Taken (per Q)':<30} | {'Score Awarded':<15}")
    print("-" * 60)
    print(f"{'0  - 10 seconds':<30} | {'100 Marks':<15}")
    print(f"{'11 - 15 seconds':<30} | {' 80 Marks':<15}")
    print(f"{'16 - 20 seconds':<30} | {' 70 Marks':<15}")
    print(f"{'21 - 30 seconds':<30} | {' 60 Marks':<15}")
    print(f"{'over 30 seconds' :<30} | {' 00 Marks':<15}")
    
    print("-" * 60)
    print(f"* Incorrect Answer: {'0 Marks':>33}")
    
    print(f"\n[{'SPEED RUN BONUSES':^25}]")
    print("Accumulated time across all questions determines final bonus:")
    print("-" * 60)
    
    print(f"1. GOLD TIER (+100 Marks):")
    print(f"   Finish ALL {total_questions} questions in under {format_time(gold_bonus_min)}")
    print(f"   (Logic: Total Time < Total Questions / 3)")
    
    print(f"\n2. SILVER TIER (+50 Marks):")
    print(f"   Finish ALL {total_questions} questions in under {format_time(silver_bonus_min)}")
    print(f"   (Logic: Total Time < Total Questions / 2)")
    
    print("-" * 60)
    print(f"{'Every Second Counts. Good Luck!':^60}")
    print("="*60 + "\n")
#intro to the game & stsrt
print("welcome to the fun quiz")
name=input("what should i call u? -> ").lower()
print(f"do i need to tell u the rules, u fool {name}")
rules=input("click y for yes , anything else for no -> ")
if rules=="y":
    print(f"as u wish, {name}")
    display_quiz_rules(10)
else:
    print(f"good ,{name}")
    flag=0
time.sleep(1)
def quiz():
    num_of_round=int(input("how many rounds u wanna play for -> "))
       
    print()
    
    
    
    #lets start 
    
    time.sleep(1)
    i=1
    final_score=0
    final_time=0

    while i<num_of_round+1:
        random_ques=random.choice(ques_list)
        ques_list.remove(random_ques)
        correct_ans=ques_ans_dict.get(random_ques).lower()
        print(f"Q{i}) {random_ques}" )
        time.sleep(1)
        start_time=time.time()
        ans_given=input("enter your answer -> ").lower()
        end_time=time.time()
        without_rounded_time=end_time-start_time
        total_time=round(without_rounded_time,3)
        if ans_given==correct_ans:
            if total_time<=10.00:
                score=100
            elif total_time<=15.00:
                score=80
            elif total_time<=20.00:
                score=70
            elif total_time<=30.00:
                score=60
            else:
                score=50
                
            print("you are correct")
            print(f"you took {total_time} sec , you got {score} points")
            final_score+=score
            final_time+=total_time
            i+=1
            
    
        else:
            print(f"you are wrong , correct answer is {correct_ans}")
            time.sleep(1)
            print(f"you took {total_time} sec , you got 0 points")
            i+=1
            final_time+=total_time
        time.sleep(1)
        print()
        if i!=num_of_round+1:
            print("get ready for next question ")
        else:
            print("thanks for playing")


        
        print()
        time.sleep(1)
    print("game end")
    print()
    if final_time<=(num_of_round)*60/3:
        final_score+=100
    elif final_time<=(num_of_round)*60/2:
        final_score+=50
    elif final_time<=(num_of_round)*60/1.5:
        final_score+=30
    print (f"your total score -> {final_score} , you took {final_time} seconds ")
    print("thanks for playing")
    
   
quiz()  


        
    

















 
