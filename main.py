import random
import sys
import os


botscore = 0
userscore = 0


print('rock = 1 paper = 2 scissors = 3')
print('First to 5 wins!')
user = int(input('choose: '))

while True:

    if user == 1:
        bot = random.randint(1, 3)
        print('You chose rock!')
        print('Bot chose...')
        if bot == 1:
            print('Rock!')
            print('It\'s a tie!')
        if bot == 2:
            print('Paper!')
            print('You lose!')
            botscore += 1
        if bot == 3:
            print('Scissors!')
            print('You win')
            userscore += 1
        user = int(input('choose: '))

    if user == 2:
        bot = random.randint(1, 3)
        print('You chose paper!')
        print('Bot chose...')
        if bot == 1:
            print('Rock!')
            print('You win!')
            userscore += 1
        if bot == 2:
            print('Paper!')
            print('It\'s a tie!')
        if bot == 3:
            print('Scissors!')
            print('You lose!')
            botscore += 1
        user = int(input('choose: '))

    if user == 3:
        bot = random.randint(1, 3)
        print('You chose scissors!')
        print('Bot chose...')
        if bot == 1:
            print('Rock!')
            print('You lose')
            botscore += 1
        if bot == 2:
            print('Paper!')
            print('You win')
            userscore += 1
        if bot == 3:
            print('Scissors!')
            print('It\'s a tie')
        user = int(input('choose: '))

    if userscore == 5:
        print('You got a score of 5 first! You win!')
        break
    if botscore == 5:
        print('Bot got a score of 5 first! You lose!')
        break
