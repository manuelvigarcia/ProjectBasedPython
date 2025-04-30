import random

computer_no=random.randint(1,20)

def sameno(target,number):
    if target == number:
        result = 'Win'

    elif target>number:
        result = 'Low'
    
    else:
        result = 'High'
    
    return result


print ("Let's guess a number between 1 and 20")

guesses_taken = 0

while guesses_taken < 5:
    guess = int(input("What is your guess? "))
    guesses_taken = guesses_taken + 1
    high_or_low = sameno(computer_no, guess)

    if high_or_low == 'Low':
        print("Too low. Try again.",end= " ")
    elif high_or_low == 'High':
        print("Too high. Try again.", end=" ")
    else:
        break
input('your score is ' + str (6 - guesses_taken))
