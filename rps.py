# Rock paper scissors game

import random
choices = ['rock', 'paper', 'scissors']
userscore = 0
pcscore = 0
gameround = 0

for gameround in range(11):
    print('Round:', gameround, ' Score: user:', userscore, 'pc:', pcscore)

    # game variables
    userChoice = input('rock, paper, or scissors?')
    pcChoice = random.randint(0, 2)
    pcChoiceText = choices[pcChoice]

    # if user picks rock
    if userChoice == 'rock':
        print('user chose ' + userChoice)
        if pcChoiceText == 'rock':
            print('pc chose rock')
            print('it was a tie!')
        if pcChoiceText == 'paper':
            print('pc chose paper')
            print('pc won!')
            pcscore = pcscore + 1
        if pcChoiceText == 'scissors':
            print('pc chose scissors')
            print('user won!')
            userscore = userscore + 1
    # if user picks paper
    if userChoice == 'paper':
        print('user chose ' + userChoice)
        if pcChoiceText == 'rock':
            print('pc chose rock')
            print('user won!')
            userscore = userscore + 1
        if pcChoiceText == 'paper':
            print('pc chose paper')
            print('it was a tie!')
        if pcChoiceText == 'scissors':
            print('pc chose scissors')
            print('pc won!')
            pcscore = pcscore + 1
    # if user picks scissors
    if userChoice == 'scissors':
        print('user chose ' + userChoice)
        if pcChoiceText == 'rock':
            print('pc chose rock')
            print('pc won!')
            pcscore = pcscore + 1
        if pcChoiceText == 'paper':
            print('pc chose paper')
            print('pc won!')
            pcscore = pcscore + 1
        if pcChoiceText == 'scissors':
            print('pc chose scissors')
            print('it was a tie!')
            print('pc won!')
            pcscore = pcscore + 1
print('Results: userscore:', userscore, 'pcScore:', pcscore)
