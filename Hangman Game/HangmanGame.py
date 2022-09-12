import os
import platform

def DrawHangman(chance): 
    if chance == 5:
        print("""
        _____________
        |           |
        |          
        | 
        |
        |
        |
     ---------
        """)
    elif chance == 4:
        print("""
        _____________
        |           |
        |          (_)
        | 
        |
        |
        |
     ---------
        """)
    elif chance == 3:
        print("""
        _____________
        |           |
        |          (_)
        |           |
        |               
        |
        |
     ---------
        """)
    elif chance == 2:
        print("""
        _____________
        |           |
        |          (_)
        |           |
        |           |    
        |          
        |         
     ---------
        """)
    elif chance == 1:
        print("""
        _____________
        |           |
        |          (_)
        |           |
        |           |    
        |          / \\
        |         
     ---------
        """)
    else:
        print("""
        _____________
        |           |
        |          (_)
        |          \\|/
        |           |    
        |          / \\
        |         
     ---------
        """)
def TypeWords(correctTries, Truth): #To type remaining mysterious letter
    global score
    for i in Truth:
        if i.lower() in correctTries:
            print(i, end="")
        else:
            print('-', end="")
def CheckWords(answer, Truth): #Checking if your guess is correct or not
    global chance, correctTries
    if answer in correctTries:
        chance -= 1
    elif answer in Truth.lower():
        correctTries.append(answer)
    else :
        chance -= 1

#Checking OS type
if platform.system() == 'Windows':
    cleans = 'cls'
else :
    cleans = 'clear'
    
score = 0
Truth = str(input("The Answer = "))
words = []
for word in Truth.lower(): #Count letters in correct answer
    if word in words:
        continue
    else:
        words.append(word)
chance = 5
correctTries = [] 
while score == 0 and chance > 0: #Game is here
    os.system(cleans)
    DrawHangman(chance)
    print('')
    print(f"\nYou have {chance} more chance..")
    TypeWords(correctTries, Truth)
    answer = str(input('\nType your guess (letter) = ')) 
    if len(answer)>1:
        print('\nType only a letter')
        os.system('pause')
    CheckWords(answer.lower(), Truth)
    if len(correctTries) == len(words): #Condition checking if you win or not
        score = 1
if chance == 0: #You lose
    os.system(cleans)
    DrawHangman(chance)
    print(f"\nYou have {chance} more chance..")
    TypeWords(correctTries, Truth)
    print('\n---- GAME OVER ----')
    os.system('pause')
elif score == 1 and chance > 0: #You win
    os.system(cleans)
    DrawHangman(chance)
    print('')
    print(f"\nYou have {chance} more chance..")
    TypeWords(correctTries, Truth)
    print('\n---- WINNER ----')