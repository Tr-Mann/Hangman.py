# Author: Tristan Mann
# Date: September 4th 2024 2:00 - September 4th 2024 6:40
# Desc: Hangman game in python (My first python project)


import os

word = ""
dispWord = ""
temp = ""
i = 0
turns = 5
win = False

# prompt for user input
print("Please enter a single word with no spaces for the player to guess: ")
#Get word to guess
word = input()
#Convert to lowercase for easier checking
word = word.lower()
for char in word:
    dispWord = ['_'] * len(word)

print("Enter the number of turns the player gets to guess the word minimum 3: ")
#Get input for turns as a string
turns = input()
#Convert turns from string to int so it can be used as a counter
turns = int(turns)
while turns < 3:
    print("Minimum number of turns is 3 try again: ")
    turns = input()
    turns = int(turns)

#Clear console so player2 can't see the word
os.system('cls')

#Reset i to use as index

while turns > 0:
    #Reset counters
    correct = 0
    
    #Concatenate output to include string and turns variable
    #Join dispWord list with spaces for display
    print(' '.join(dispWord))  
    print(f"You have {turns} turns left")
    print("Guess a letter: ")
    #Convert input to lowercase
    
    if len(temp) != 1 or not temp.isalpha():
        print("Please enter a single letter.")
        continue
    
    found = False
    for i, char in enumerate(word):
        if char == temp:
            #Update the display word
            dispWord[i] = temp  
            correct += 1
            found = True
    
    if found:
        print("You guessed one or more correct letter(s)!")
        turns -= 1
    else:
        turns -= 1
        print("That letter is not in the word.")
    
    if '_' not in dispWord:
        print(f"Congratulations! You've guessed the word: {''.join(dispWord)}")
        break
if turns == 0:
    print("Try to guess the word:")
    temp = input()
    if temp == word:
        print("You Win!!!")
        win = True

if '_' in dispWord and win == False:
    print("You're out of turns and did not guess the word!")
