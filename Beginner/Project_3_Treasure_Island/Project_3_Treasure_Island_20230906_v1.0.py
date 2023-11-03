print('''
      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
                dwb `---`
''')
print("Welcome to Treasure Island")
print("Your Mission is to find the Treasure!")

stage_one = input("\nYou've just landed on the island. Do you want to explore the right side of the island or the left side of the island first? Type Right or type Left ").lower()
if stage_one == "left":
  stage_two = input("\nSuccess! You decided to go right and have reached the jungle with a river flowing through. Do you want to wait or swim? Type Wait or type Swim ").lower()
  if stage_two == "wait":
    stage_three = input("\nWhich door do you want to go through? Blue? Red? Yellow? Your know what to do. ").lower()
    if stage_three == "red":
      print("\nYou've been burned by fire. Game Over!")
    elif stage_three == "blue":
      print("\nYou've been eaten by beasts. Game Over!")
    elif stage_three == "yellow":
      print("\nYou win!")
    else:
      print("\nYou were captured by pirates. Game Over!")
  else:
    print("\nYou've been attacked by agile and deadly sharks with razor-sharp teeth. Game Over!")
else: 
  print("\nYou decided to go a different direction and after a minute, you've suddenly been wrapped in eternal darkness. You can't get out of it. Game over!")

    
