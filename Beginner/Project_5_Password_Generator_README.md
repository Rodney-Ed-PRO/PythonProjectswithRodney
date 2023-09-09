👋 This is my fifth Python Project called Password Generator! As the name suggests, this program will help the user create a password! There are two versions of the password that the program will provide the user: One that is easy where the program will generate a password according to the user's requirement for the amount of each character type (i.e. letters, number, and symbols) but in the order of the question being asked. 
Another version of the password will shuffle the characters of the password so that it is more robust. 

🐍 Here are the lessons I applied within this lesson and project:
* Loops
    'for item in list_of_items:
        do something'
    Each item in the list is given a variable name 
    The for loop allows you to execute the same line of code or operation multiple times
* For Loops and the range() function
    * this is useful when you aren't working with lists
* Randomization:
    * import random module
    * to call on a random item in the list of letters, numbers, and symbols I used the random.randint() function
    * in the hard version of the password which required the characters to being organized in random order, I created two versions of it:
        * the first hard version of the password created a new list in which all the random elements of the password were appended to the empty list and then the items in the list were shuffled using the random.shuffle() function 
        Then, I converted the items in the list to a string on one line using an empty string variable and add each element in the shuffled list 
        * Alternatively, I created an empty string variable and concatenated each password character to the variable. I then used a new function ''.join(random.sample(hard_password,len(hard_password))) to produce the string of characters in random order


📂 Additional Comments:
* randomization is useful in many ways. It can be used to create fun games like tetris where the blocks that fall down are unpredictable and different shapes. It can also be used to create hacker-proof, secure passwords for user security. 





