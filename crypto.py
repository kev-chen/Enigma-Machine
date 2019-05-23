#!/usr/bin/python3
import string
from util import rotate

class Enigma:
    def __init__(self, key1, key2):
        self.forwardPlugboard = dict()
        self.backwardPlugboard = dict()

        for i in range(len(key1)):
            self.forwardPlugboard[key1[i]] = key2[i]
            self.backwardPlugboard[key2[i]] = key1[i]

        self.rightWheel = ['3', '5', 'h', 'e', 'f', 'g', 'd', 'q', '8', 'm', '2', 'k', 'l', 'j', 'n', 's', 'u', 'w', 'o', 'v', 'r', 'x', 'z', 'c', 'i', '9', 't', '7', 'b', 'p', 'a', '0', '1', 'y', '6', '4']
        self.middleWheel = ['0', 'l', 'x', '1', '2', '8', 'h', 'b', '3', 'n', 'r', 'o', 'k', 'd', 't', '7', 'c', '6', 'p', 'i', 'v', 'j', '4', 'a', 'u', 'w', 'm', 'e', '9', '5', 'q', 's', 'z', 'g', 'y', 'f']
        self.leftWheel = ['2', 'y', 'z', '0', '1', 'a', 'w', 'i', 'p', 'k', 's', 'n', '3', 't', 'e', 'r', 'm', 'u', 'c', '5', 'v', '6', 'x', '7', 'f', 'q', 'o', 'l', '4', '8', 'g', 'd', '9', 'b', 'j', 'h']
        self.encryptionReflector = self.forwardPlugboard
        self.decryptionReflector = self.backwardPlugboard
        self.characters = dict()

        index = 0
        for char in string.ascii_uppercase:
            self.characters[char] = index
            index += 1

        for num in range(10):
            self.characters[char(num)] = index
            index += 1
        
        self.mode = 'ENCRYPT'

    def setToEncrypt(self):
        self.mode = 'ENCRYPT'


    def setToDecrypt(self):
        self.mode = 'DECRYPT'



    def encrypt(self, input):
        strBuffer = list()
        leftWheel = self.leftWheel
        middleWheel = self.middleWheel
        rightWheel = self.rightWheel
        numCharactersTyped = 0
        for char in input:
            numCharactersTyped += 1
            strBuffer.append( self.getEncryptedCharacter(char, leftWheel, middleWheel, rightWheel) )
            self.rotateWheelsForward(numCharactersTyped, leftWheel, middleWheel, rightWheel)
        
        return ''.join(strBuffer)



    def decrypt(self, input):
        strBuffer = [None] * len(input)
        leftWheel = self.leftWheel
        middleWheel = self.middleWheel
        rightWheel = self.rightWheel

        # Initialize wheel rotations to the last rotated position
        for i in range(len(input)):
            self.rotateWheelsForward(i, leftWheel, middleWheel, rightWheel)

        numCharactersTyped = len(input) - 1
        
        # Go backwards to decrypt
        for i in range(len(input)-1, -1, -1):
            strBuffer[i] = self.getDecryptedCharacter(input[i], leftWheel, middleWheel, rightWheel)
            self.rotateWheelsBackward(numCharactersTyped, leftWheel, middleWheel, rightWheel)
            numCharactersTyped -= 1
        
        return ''.join(strBuffer)




    def getEncryptedCharacter(self, char, leftWheel, middleWheel, rightWheel):
        # 1. Get the character
        encryptedChar = char

        # 2. Pass through plugboard
        encryptedChar = self.forwardPlugboard[encryptedChar]

        # 3. Pass through wheels
        index = self.characters[encryptedChar.upper()]
        encryptedChar = rightWheel[index]

        index = self.characters[encryptedChar.upper()]
        encryptedChar = middleWheel[index]

        index = self.characters[encryptedChar.upper()]
        encryptedChar = leftWheel[index]

        encryptedChar = encryptionReflector[encryptedChar.upper()]

        index = self.characters[encryptedChar.upper()]
        encryptedChar = leftWheel[index]

        index = self.characters[encryptedChar.upper()]
        encryptedChar = middleWheel[index]

        index = self.characters[encryptedChar.upper()]
        encryptedChar = rightWheel[index]

        # 4. Pass back through plugboard
        encryptedChar = self.backwardPlugboard[encryptedChar.upper()]


        return encryptedChar





    def rotateWheelsForward(numCharactersTyped, leftWheel, middleWheel, rightWheel):
        rightWheel = rotate(rightWheel, 1)
        
        if numCharactersTyped % 7 == 0:
            middleWheel = rotate(middleWheel, 1)
        
        if numCharactersTyped % 5 == 0:
            leftWheel = rotate(leftWheel, 1)





    def rotateWheelsBackward(numCharactersTyped, leftWheel, middleWheel, rightWheel):
        rightWheel = rotate(rightWheel, -1)
        
        if numCharactersTyped % 7 == 0:
            middleWheel = rotate(middleWheel, -1)
        
        if numCharactersTyped % 5 == 0:
            leftWheel = rotate(leftWheel, -1)

    

    

def main():
    # REPL here
    pass

if __name__ == "__main__":
    main()