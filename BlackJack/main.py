# Blackjack
import random
import art
############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

restart = True

while restart == True:

    gameCont = True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def dealCard(cards):
        rCard = random.choice(cards)
        return rCard

    User = []
    Comp = []
    u1 = dealCard(cards)
    u2 = dealCard(cards)
    c1 = dealCard(cards)
    c2 = dealCard(cards)

    User.append(u1)
    User.append(u2)
    Comp.append(c1)
    Comp.append(c2)

    print(art.logo)
    print(f'User cards are {User}')
    print(f'Comp cards are {Comp}')


    def calcScore(list):
        Score = sum(list)
        if Score == 21 and len(list) == 2:
            return 0
        if Score > 21 and len(list) > 2 and 11 in list:
            list.remove(11)
            list.append(1)
        Score = sum(list)
        return Score


    while gameCont:
        sumUser = calcScore(User)
        sumComp = calcScore(Comp)
        if sumUser == 0:
            print("User Wins, Blackjack")
            print("Game Over")
            gameCont = False
            break
        elif sumComp == 0:
            print("User Loses, Computer has Blackjack")
            print("Game Over")
            gameCont = False
            break

        anotherCard = input('Would user like to draw another card? Type yes or no \n')
        if sum(User) < 21:
            if anotherCard == 'yes':
               randCard = dealCard(cards)
               User.append(randCard)
            if sum(User) > 21:
                gameCont = False
        if sum(User) == 21:
            gameCont = False
        elif anotherCard == 'no':
            newSum = sum(Comp)
            while sum(Comp) < 17:
                randCard = dealCard(cards)
                Comp.append(randCard)
                gameCont = False
                newSum = sum(Comp)
        sumUser = sum(User)
        sumComp = sum(Comp)

        print(f'User cards are {User}, Score is {sumUser}')
        print(f'Comp cards are {Comp}, Score is {sumComp}')


    After = True
    while After:
        if sumComp > 21:
            print("User Wins")
            After = False
            break
        if sumUser > 21:
            print("User Loses")
            After = False
            break
        if sumUser == 21:
            print("User Wins, Blackjack")
            After = False
            break
        if sumComp == 21:
            print("Comp Wins, Blackjack")
            After = False
            break
        elif sumComp > sumUser:
            print("Comp Wins")
            After = False
            break
        elif sumUser > sumComp:
            print("User Wins")
            After = False
            break
        elif sumUser == sumComp:
            print("Draw")
            After = False
            break

    restart = input("Does user want to restart the game? Type yes or no\n")
    if restart == 'no':
        restart = False
        break
    else:
        restart = True

print('Game Over!')

