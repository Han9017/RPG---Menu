#------------------------------------------------------------------------------
#    File name: Simple Menu
#    Author: Han Wang
#    Date created: 3/10/2023
#    Date last modified: 3/13/2023
#------------------------------------------------------------------------------
'''   Description: Simple game Menu '''
#------------------------------------------------------------------------------
print("Valid actions for current location")
print("Go in one of the following directions:")
Directions = ["north", "south", "west", "east"]
for go in Directions:
  print(f"* {go.title()}")
print("Complete one of the following actions:")

Actions = ["expore", "attack", "defend", "heal", "quit"]
for do in Actions:
  print(f"* {do.title()}")
userInput = input("Enter an action: ").lower()
#player input 'quit'
while userInput != 'quit':
  validInput = False
#player valid input
  
  for go in Directions:
    if userInput == go:
      print(f"Go {go.title()}!")
      validInput = True
      
  for do in Actions:
    if userInput == do:
      print(f"{do.title()}!")
      validInput = True

  if validInput == False:
    print("Invalid input!")
    
  userInput = input("Enter an action: ").lower()
