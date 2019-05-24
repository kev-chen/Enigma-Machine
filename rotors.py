#!/usr/bin/python3

from config import Config
from util import rotate

class Rotors:
    def __init__(self, left, middle, right, key3):
        # Keep track of the original positions
        self.originalLeftRotor = rotate([ch.upper() for ch in left], Config.setting('characters')[key3[0]])
        self.originalMiddleRotor = rotate([ch.upper() for ch in middle], Config.setting('characters')[key3[1]])
        self.originalRightRotor = rotate([ch.upper() for ch in right], Config.setting('characters')[key3[2]])

        # Rotate these when encrypting/decrypting
        self.leftRotor = self.originalLeftRotor
        self.middleRotor = self.originalMiddleRotor
        self.rightRotor = self.originalRightRotor
        self.setRotorWiring(self.leftRotor, self.middleRotor, self.rightRotor)



    '''
     Sets the wheel mappings between wheels
    '''
    def setRotorWiring(self, left, middle, right):
        availableCharacters = list(Config.setting('characters').keys())

        self.rightForward = dict(zip(availableCharacters, right))
        self.rightBackward = { value: key for key,value in self.rightForward.items() }

        self.middleForward = dict(zip(availableCharacters, middle))
        self.middleBackward = { value: key for key,value in self.middleForward.items() }

        self.leftForward = dict(zip(availableCharacters, left))
        self.leftBackward = { value: key for key,value in self.leftForward.items() }



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
        