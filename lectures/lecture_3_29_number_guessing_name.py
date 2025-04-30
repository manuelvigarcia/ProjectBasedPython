import random

def sameno(target,guess):
    if target==guess:
        result='Win'
    else:
        result = 'Fail'
    return result


number = random.randint(1, 20)
print(number)

print ("let's guess a number")

guess = int(input("what is your guess? "))

print(sameno(number,guess))

