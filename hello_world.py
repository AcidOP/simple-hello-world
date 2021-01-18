from time import *
from random import *

class Class:
    def __init__(self):
        self.hello = [72, 69, 76, 76, 79, 87, 79, 82, 76, 68]
        self.dontKnowWhatTheFuckArray = []
        self.big_A_to_big_Z_ascii = []
        self.big_A_to_big_Z = []
        self.xx = 65
        self.xxx = 90
        self.timer = 0.5
        self.result = ''
        self.display = ''
        self.count = 0
        self.check = True
        self.update_big_A_to_big_Z()
        self.ascii_to_letter()

    def update_big_A_to_big_Z(self):
        for i in range(self.xx, self.xxx+1):
            self.dontKnowWhatTheFuckArray.append(i)
        self.big_A_to_big_Z_ascii.extend(self.dontKnowWhatTheFuckArray)

    def ascii_to_letter(self):
        for integer in self.big_A_to_big_Z_ascii:
            self.big_A_to_big_Z.append(chr(integer))

    def takeLetter(self):
        takeYourCHance = ''.join(choice(self.big_A_to_big_Z))
        return takeYourCHance

    def bruteForce(self):
        while self.check:
            sleep(self.timer)
            takeYourChanceAgain = Class.takeLetter(self)
            print(takeYourChanceAgain)

            if (takeYourChanceAgain == chr(self.hello[self.count])):
                self.display += takeYourChanceAgain
                self.display += ' '
                self.result += takeYourChanceAgain
                print(self.display)
                self.count += 1

                if (self.result == 'HELLOWORLD'):
                    self.check = False
                    return self.check

xxx = Class()
xxx.bruteForce()
