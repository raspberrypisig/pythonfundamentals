import random
userinput = str(input("Choose rock, paper or scissor:"))
print("User selection:" , userinput) 	
valid_responses = ["rock", "paper", "scissor"]
if userinput in valid_responses:
    print("user input is valid")
else:
    print("user input is invalid")

computer_choice = random.choice(valid_responses)
print("Computer selection:",computer_choice)

results = {"rock":"scissor", "paper": "rock", "scissor":"paper"}
print(type(results))
b = results[userinput]

if userinput == computer_choice:
   print("It's a tie")

elif b == None:
    print("Computer won")
  
else:
    print("User won") 







def rockscissorspaper():
    pass
'''
def add(x,y):
    return x + y
	
b = input("Type a number")
print(b)	
c = add(100, b)
print(c)
'''	
	

