# -*- coding: utf-8 -*-

import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 2] * 4

random.shuffle(cards)


class Game1:
    def __init__(self):
        self.count = 0
        self.current1 = cards.pop()
        self.count += self.current1
        self.current2 = cards.pop()
        self.count += self.current2
        print "Your cards are ", self.current1, self.current2
        print "Total score  ", self.count

        while self.count < 21:
            self.choice = raw_input("Will you take another card? y/n\n")
            if self.choice == 'y':
                self.current3 = cards.pop()
                self.count += self.current3
                print "Your card is", self.current3
                print "Total score", self.count
                if self.count == 21:
                    print "Black Jack! You win!"
                if self.count > 21:
                    print "You lost, try again!", self.count
                    break
            elif self.choice == 'n':
                print "Try again later!"
                break


class Game2:
    def __init__(self):
        self.count = 0
        self.current1 = cards.pop()
        self.count += self.current1
        self.current2 = cards.pop()
        self.count += self.current2
        print "Computer cards are ", self.current1, self.current2
        print "Computer score", self.count

        while self.count < 21:
            if self.count <= 8:
                self.current3 = cards.pop()
                self.count += self.current3
                print "Computer card is", self.current3
                print "Computer score", self.count
                if self.count == 21:
                    print "Black Jack! Computer wins!"
                elif self.count > 21:
                    print "Computer lost", self.count
                    break
            elif 8 < self.count < 20:
                self.choice = random.randint(1, 2)
                if self.choice == 1:
                    self.current3 = cards.pop()
                    self.count += self.current3
                    print "Computer card is", self.current3
                    print "Computer score", self.count
                    if self.count == 21:
                        print "Black Jack! Computer wins!"
                    if self.count > 21:
                        print "Computer lost, try again!", self.count
                        break
            else:
                print "Computer score", self.count
                break


player1 = Game1
player2 = Game2

player1()
player2()