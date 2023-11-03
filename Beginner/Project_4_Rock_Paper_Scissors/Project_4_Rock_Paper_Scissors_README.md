👋 This is my fourth Python Project which simulates the Rock Paper Scissors game! The user will tell the program what move they choose between Rock Paper or Scissors and the computer will randomly generates its own move. The user's move and the computer's move is compared to determine if the user wins or loses. 

🐍 Here are the lessons I applied within this lesson and project:
* Randomization:
    * import random module
    * generate a random integer:
        a = random.randint(0,10)
    * generate a random floating point number:
        a = random.random() -> this only generates a number between 0 and 1, left inclusive
        * in order to generate a floating point number for number greater than 1, you can multiply random.random() by the upper end of the range you wish to have. For example, random.random() * 5. Alternatively, you can also use a combination of the random.random() and random.randint(0,5) to achieve a similar objective.
* Python lists: Data Structure **super useful as a data analyst
    * lists are useful in many instances like storing the name of all of the states in the unites states or the order of a virtual queue for example
    * fruits = [item1, item2]
    * lists are used to store many pieces of related data

    * lists begin with the index 0
    * you can call a list using square brackets following the name of the list: fruits[0]
    * you can alter items in a list by calling on the index of the list that contains that item and assigning it a different value: fruits[0] = "apple"

    * you can add to a list using the .append() function where you pass an argument as the item you wish to append/add to the end of the list: fruits.append("banana")
    * you can even add a list to a list by using the .extend() function: fruits.extend(["grapes", "strawberry"])
* Nested Lists:
    * Call an item in a nested list using two indices: grocery_list[1][2]

* Debugging:
    * Index Error 

* Helpful Resources:
    * flow chart to visually describe the control flow of the program. Helpful site is draw.io
    * ASCII art website to incorporate visuals into code 


📂 Additional Comments:
* there are so many applications when it comes to using lists in code





