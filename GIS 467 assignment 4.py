# -*- coding: utf-8 -*-
"""
1. Write a script that allows the user to enter an email address and prints the 
    domain in a message.
    In an email address, the part after the @ symbol is called the domail. (eg.
    gmail.com is the domain of python@gmail.com) The script would return gmail.com.
2. Iterate over a tuple of integers and indicate for each whether the number is 
    odd or even.
    For example:    200 is even
                    387 is odd
                    405 is odd
3. Write a script that accepts a sentece as user input and then prints out the 
    following information:
        counts all characters in the sentence
        counts all spaces in the sentence
        capitalizes every character in the sentence
        prints the index of the first space in the sentence
"""

class AssignmentFour:
    #1 email domain
    email = input("Please enter your email.\n")
    i = 0
    while i < len(email):
        if(email[i] == "@"):
            print(f"The domain is {email[i+1:]}.\n") #prints the String between the index and the end
        i+=1

    #2 odd or even integers
    nums = (200, 387, 405)
    for num in nums:
        print(f"{num} is even" if num%2 == 0 else f"{num} is odd")
    print()    
    
    #3 character analysis
    sentence = input("Please enter a sentence.\n")
    characters = 0
    spaces = 0
    firstSpace = -1
    
    for letter in sentence:
        characters += 1
        if(letter == " "):
            spaces += 1
            if(firstSpace == -1):
                firstSpace = sentence.index(letter) #find the index of the character
    
    print(f"There are {characters} characters")
    print(f"There are {spaces} spaces.")
    print(f"The first space is at {firstSpace}.")
    print(f"The sentence is now in uppercase:\n\t{sentence.upper()}")
           
    input("Press enter to exit.")