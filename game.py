# -*- coding: utf-8 -*-

import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

random.shuffle(cards)

print "Lets play BlackJack!"
count = 0

current1 = cards.pop()
count += current1
current2 = cards.pop()
count += current2

print "Your cards are ", current1, current2
print "Total score  ", count


while count < 21:
    choice = input("Will you take another card? y/n\n")
    if choice == 'y':
        current3 = cards.pop()
        count+=current3
        print "Your card is", current3
        print "Total score", count
        if count == 21:
            print "Black Jack! You win!"
        if count > 21:
            print "You lost, try again!", count
            break
    if choice == 'n':
        print "Try again later!"
        break