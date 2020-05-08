import random

tries, random_num = 0, random.randint(1,100)
result = True
while result == True:
    print('Guess a number range 1- 100')
    guess = int(input('>>>'))
    if guess > random_num:
        print('{} is greater than number X'.format(guess))
        tries +=1
    elif guess < random_num:
        print('{} is smaller than number X'.format(guess))
        tries +=1
    else:
        tries +=1
        print('You\'re right. The number is {}.\nYou guessed the correct number in {} guesses'.format(random_num, tries))
        result = False
        