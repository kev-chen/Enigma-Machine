#!/usr/bin/python3
import string
from util import rotate
from rotors import Rotors
from config import Config

class Enigma:
    def __init__(self, key1, key2, key3):
        self.forwardPlugboard = dict(zip(key1, key2))
        self.backwardPlugboard = { value: key for key,value in self.forwardPlugboard.items() }
        self.forwardReflector = self.forwardPlugboard
        self.backwardReflector = self.backwardPlugboard
        self.rotors = Rotors(Config.setting('leftRotor'), Config.setting('middleRotor'), Config.setting('rightRotor'), key3)


                        
    '''
     Encrypts an entire input string
    '''
    def encrypt(self, input):
        strBuffer = list()
        numCharactersTyped = 0
        for char in input:
            numCharactersTyped += 1
            strBuffer.append( self.getEncryptedValue(char.upper()) )
            self.rotors.rotateForward(numCharactersTyped)
        
        self.rotors.reset()
        
        return ''.join(strBuffer)



    '''
     Decrypts an entire input string
    '''
    def decrypt(self, input):
        strBuffer = list()
        numCharactersTyped = 0
        for char in input:
            numCharactersTyped += 1
            strBuffer.append( self.getDecryptedValue(char.upper()) )
            self.rotors.rotateForward(numCharactersTyped)

        self.rotors.reset()
        
        return ''.join(strBuffer)



    '''
     Encrypts a single character according to the state of the wheel rotations
    '''
    def getEncryptedValue(self, char):
        # 1. Get the character
        encryptedChar = char

        # 2. Pass through plugboard
        encryptedChar = self.forwardPlugboard[encryptedChar]

        # 3. Pass through wheels
        encryptedChar = self.passThroughRight2Left(encryptedChar)
        encryptedChar = self.forwardReflector[encryptedChar]
        encryptedChar = self.passThroughLeft2Right(encryptedChar)

        # 4. Pass back through plugboard
        encryptedChar = self.backwardPlugboard[encryptedChar.upper()]

        return encryptedChar



    '''
     Decrypts a single character according to the state of the wheel rotations
    '''
    def getDecryptedValue(self, char):
        # 1. Get the character
        encryptedChar = char

        # 2. Pass through plugboard 
        encryptedChar = self.forwardPlugboard[encryptedChar]

        # 3. Pass through wheels
        encryptedChar = self.passThroughRight2Left(encryptedChar)
        encryptedChar = self.backwardReflector[encryptedChar]
        encryptedChar = self.passThroughLeft2Right(encryptedChar)

        # 4. Pass back through plugboard
        encryptedChar = self.backwardPlugboard[encryptedChar.upper()]

        return encryptedChar



    '''
     Passes through the rotors from right to left
    '''
    def passThroughRight2Left(self, char):
        entryChar = char.lower()

        returnChar = self.rotors.rightToMiddle[entryChar]
        returnChar = self.rotors.middleToLeft[returnChar]

        return returnChar.upper()



    '''
     Passes through the rotors from left to right
    '''
    def passThroughLeft2Right(self, char):
        entryChar = char.lower()

        returnChar = self.rotors.leftToMiddle[entryChar]
        returnChar = self.rotors.middleToRight[returnChar]

        return returnChar.upper()