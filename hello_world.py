import string
from time import sleep
from random import choice


class hello:

    def __init__(self):
        self.hello = ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']
        self.word = ''

    def generate(self):
        throw = ''.join(choice(string.ascii_uppercase))
        return throw

    def takeLetter(self):
        i = 0
        while True:
            sleep(0.5)
            self.letter = hello.generate(self)
            print(f'\n\t {self.letter}')

            if (self.letter == self.hello[i]):
                self.word += self.letter
                print(f'\n\t {self.word}')
                i += 1
                if (self.word == 'HELLOWORLD'):
                    return False
                
        
xxx = hello()
xxx.takeLetter()
