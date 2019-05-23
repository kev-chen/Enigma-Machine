#!/usr/bin/python3
import string
from util import rotate
from rotors import Rotors

class Enigma:
    def __init__(self, key1, key2):
        self.forwardPlugboard = dict(zip(key1, key2))
        #self.backwardPlugboard = dict(zip(key2, key1))
        self.backwardPlugboard = { value: key for key,value in self.forwardPlugboard.items() }
        self.forwardReflector = self.forwardPlugboard
        self.backwardReflector = self.backwardPlugboard

        self.rotors = Rotors( \
                        ['2', 'y', 'z', '0', '1', 'a', 'w', 'i', 'p', 'k', 's', 'n', '3', 't', 'e', 'r', 'm', 'u', 'c', '5', 'v', '6', 'x', '7', 'f', 'q', 'o', 'l', '4', '8', 'g', 'd', '9', 'b', 'j', 'h'], \
                        ['0', 'l', 'x', '1', '2', '8', 'h', 'b', '3', 'n', 'r', 'o', 'k', 'd', 't', '7', 'c', '6', 'p', 'i', 'v', 'j', '4', 'a', 'u', 'w', 'm', 'e', '9', '5', 'q', 's', 'z', 'g', 'y', 'f'], \
                        ['3', '5', 'h', 'e', 'f', 'g', 'd', 'q', '8', 'm', '2', 'k', 'l', 'j', 'n', 's', 'u', 'w', 'o', 'v', 'r', 'x', 'z', 'c', 'i', '9', 't', '7', 'b', 'p', 'a', '0', '1', 'y', '6', '4'], \
                        '123')

        self.characters = dict(zip([ch for ch in string.ascii_uppercase] + [str(num) for num in range(10)], list(range(36))))



    def encrypt(self, input):
        strBuffer = list()
        numCharactersTyped = 0
        for char in input:
            numCharactersTyped += 1
            strBuffer.append( self.getEncryptedValue(char.upper()) )
            self.rotors.rotateForward(numCharactersTyped)
        
        self.rotors.reset()
        
        return ''.join(strBuffer)



    def decrypt(self, input):
        strBuffer = list()
        numCharactersTyped = 0
        for char in input:
            numCharactersTyped += 1
            strBuffer.append( self.getDecryptedValue(char.upper()) )
            self.rotors.rotateForward(numCharactersTyped)

        self.rotors.reset()
        
        return ''.join(strBuffer)

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


    def passThroughRight2Left(self, char):
        #charIndex = self.characters[char.upper()]

        #entryChar = self.rotors.rightWheel[charIndex]
        entryChar = char.lower()

        returnChar = self.rotors.rightToMiddle[entryChar]
        returnChar = self.rotors.middleToLeft[returnChar]

        return returnChar.upper()



    def passThroughLeft2Right(self, char):
        # charIndex = self.characters[char.upper()]

        # returnChar = self.rotors.leftWheel[charIndex]
        entryChar = char.lower()

        returnChar = self.rotors.leftToMiddle[entryChar]
        returnChar = self.rotors.middleToRight[returnChar]

        return returnChar.upper()