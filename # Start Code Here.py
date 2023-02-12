# Start Code Here
import random  # Resets Everything
score = 0
computer_score = 0
bot_behaviour = 0
behaviour_chosen = False
rock_total = 0
paper_total = 0
scissors_total = 0
rock_priority = 0
paper_priority = 0
scissors_priority = 0
complex_maths_stuff = 0
final_stretch = False
while True:
  if behaviour_chosen == False: # Difficulty Selection
    user_action = input("Enter a difficulty (odd, strategy-based):")
    possible_actions = ["odd", "strategy-based"]
    computer_action = "rock"
    print("Choose Difficulty")
    print(user_action)
    if user_action == "odd":
      behaviour_chosen = True
      bot_behaviour = 1
    if user_action == "strategy-based":
      behaviour_chosen = True
      bot_behaviour = 2
  if behaviour_chosen == True: # The Actual Game Starts
   user_action = input("Enter a choice (rock, paper, scissors):")
   possible_actions = ["rock", "paper", "scissors"]
   def Strat_Calculator():
      if bot_behaviour == 1: # The Computer's Decisions Are Completely Random
       computer_action = random.choice(possible_actions)
   if bot_behaviour == 2: # The Computer's Decision Is Based Off A Random Number Generator, Each Number Represents A Probability/Value
     if rock_total >= paper_total and scissors_total: # Decides The Probability If You Use Rock The Most
       rock_priority = 5
       paper_priority = 7
       scissors_priority = 9
     else:
       if paper_total >= rock_total and scissors_total: # Decides The Probability If You Use Paper The Most
         paper_priority = 5
         rock_priority = 7
         scissors_priority = 9
       else:
         if scissors_total >= rock_total and paper_total: # Decides The Probability If You Use Scissors The Most
           scissors_priority = 3
           rock_priority = 6
           scissors_priority = 9
         else:
           rock_priority = 3
           paper_priority = 3
           scissors_priority = 3
     complex_maths_stuff = random.randint(1, 9) # Decides The Probability If The Game Just Started
     if rock_total >= paper_total and scissors_total:
       if complex_maths_stuff >= 0 and complex_maths_stuff <= 4:
        computer_action = "rock"
       else:
        if complex_maths_stuff >= 3 and complex_maths_stuff <= 8:
         computer_action = "paper"
        else:
         if complex_maths_stuff >= 7 and complex_maths_stuff <=10:
           computer_action = "scissors"
     if paper_total >= rock_total and scissors_total:
       if complex_maths_stuff >= 0 and complex_maths_stuff <= 4:
        computer_action = "paper"
       else:
        if complex_maths_stuff >= 3 and complex_maths_stuff <= 8:
         computer_action = "rock"
        else:
         if complex_maths_stuff >= 7 and complex_maths_stuff <=10:
           computer_action = "scissors"
     if scissors_total >= rock_total and paper_total:
      if rock_total >= paper_total and scissors_total:
       if complex_maths_stuff >= 0 and complex_maths_stuff <= 4:
        computer_action = "scissors"
       else:
        if complex_maths_stuff >= 3 and complex_maths_stuff <= 8:
         computer_action = "paper"
        else:
         if complex_maths_stuff >= 7 and complex_maths_stuff <=10:
           computer_action = "rock"
   Strat_Calculator()
   print("You choose")
   print(user_action)
   print("Computer choose")
   print(computer_action)
   def youVSnpc():
     print(score)
     print(computer_score)
   if user_action == computer_action:
     print("Draw!!!")
     youVSnpc()
   elif user_action == "rock":
     paper_total += 1
     if computer_action == "scissors":
       print("Rock smashes scissors. You win!!!!!!!!")
       score += 1
       youVSnpc()
     else:
       print("Paper covers rock. You lose!!!!!!!!!!!!!!!!!!!!!")
       computer_score += 1
       youVSnpc()
   elif user_action == "paper":
     scissors_total += 1
     if computer_action == "scissors":
       print("Scissors cuts paper. You lose!!!!!!!!!!!")
       computer_score += 1
       youVSnpc()
     else:
       print("Paper covers rock. You win!!!!!!!!!!!!!!!!!!!!!")
       score += 1
       youVSnpc()
   elif user_action == "scissors":
     rock_total += 1
     if computer_action == "paper":
       print("Scissors cuts paper. You win!!!!!!!!!!!")
       score += 1
       youVSnpc()
     else:
       print("Rock smashes scissors. You lose!!!!!!!!!!!!!!!!!!!!!")
       computer_score += 1
       youVSnpc()
