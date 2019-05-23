#!/usr/bin/python3

from config import Config
from util import rotate

class Rotors:
    def __init__(self, left, middle, right, key3):
        # Keep track of the original positions
        self.originalLeftRotor = rotate(left, Config.setting('characters')[key3[0]])
        self.originalMiddleRotor = rotate(middle, Config.setting('characters')[key3[1]])
        self.originalRightRotor = rotate(right, Config.setting('characters')[key3[2]])

        # Rotate these when encrypting/decrypting
        self.leftRotor = self.originalLeftRotor
        self.middleRotor = self.originalMiddleRotor
        self.rightRotor = self.originalRightRotor

        # Wiring between rotors
        self.rightToMiddle = None
        self.middleToLeft = None
        self.leftToMiddle = None
        self.middleToRight = None
        self.setRotorWiring(self.leftRotor, self.middleRotor, self.rightRotor)



    '''
     Sets the "wirings" between wheels
    '''
    def setRotorWiring(self, left, middle, right):
         # Right to left mappings
        self.rightToMiddle = dict(zip(right, middle))
        self.middleToLeft = dict(zip(middle, left))
        
        # Left to right mappings
        self.leftToMiddle = dict(zip(left, middle))
        self.middleToRight = dict(zip(middle, right))



    '''
     Rotates wheels forward based on the rotation rates of each wheel
    '''
    def rotateForward(self, numCharactersTyped):
        if numCharactersTyped % Config.setting('rightRotorRate') == 0:
            self.rightRotor = rotate(self.rightRotor, 1)
        
        if numCharactersTyped % Config.setting('middleRotorRate') == 0:
            self.middleRotor = rotate(self.middleRotor, 1)
        
        if numCharactersTyped % Config.setting('leftRotorRate') == 0:
            self.leftRotor = rotate(self.leftRotor, 1)

        self.setRotorWiring(self.leftRotor, self.middleRotor, self.rightRotor)


    '''
     Resets mappings to original configuration
    '''
    def reset(self):
        self.leftRotor = self.originalLeftRotor
        self.middleRotor = self.originalMiddleRotor
        self.rightRotor = self.originalRightRotor
        self.setRotorWiring(self.leftRotor, self.middleRotor, self.rightRotor)
        