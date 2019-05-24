#!/usr/bin/python3
import string
from util import rotate
from rotors import Rotors
from config import Config

class Enigma:
    def __init__(self, key1, key2, key3):
        self.forwardPlugboard = dict(zip(list(Config.setting('characters').keys()), key1))      # Available Characters - key1 mapping
        self.backwardPlugboard = { value: key for key,value in self.forwardPlugboard.items() }  # Inverse mapping
        self.forwardReflector = dict(zip(list(Config.setting('characters').keys()), key2))      # Available Characters - key2 mapping
        self.backwardReflector = { value: key for key,value in self.forwardReflector.items() }  # Inverse mapping
        self.rotors = Rotors(Config.setting('leftRotor'), Config.setting('middleRotor'), Config.setting('rightRotor'), key3)


                        
    '''
     Encrypts an entire input string
    '''
    def encrypt(self, input):
        try:
            strBuffer = list()
            numCharactersTyped = 0
            for char in input:
                numCharactersTyped += 1
                self.rotors.rotateForward(numCharactersTyped)
                strBuffer.append( self.getEncryptedValue(char.upper()) )
            return ''.join(strBuffer)

        except Exception as e:
            return f'Error encrypting: {str(e)}'

        finally:
            self.rotors.reset()



    '''
     Decrypts an entire input string
    '''
    def decrypt(self, input):
        try:
            strBuffer = list()
            numCharactersTyped = 0
            for char in input:
                numCharactersTyped += 1
                self.rotors.rotateForward(numCharactersTyped)
                strBuffer.append( self.getDecryptedValue(char.upper()) )
            return ''.join(strBuffer)

        except Exception as e:
            return f'Error decrypting: {str(e)}'
            
        finally:
            self.rotors.reset()



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
        encryptedChar = self.backwardPlugboard[encryptedChar]

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
        encryptedChar = self.backwardPlugboard[encryptedChar]

        return encryptedChar



    '''
     Passes through the rotors from right to left
    '''
    def passThroughRight2Left(self, char):
        returnChar = self.rotors.rightForward[char]
        returnChar = self.rotors.middleForward[returnChar]
        returnChar = self.rotors.leftForward[returnChar]

        return returnChar



    '''
     Passes through the rotors from left to right
    '''
    def passThroughLeft2Right(self, char):
        returnChar = self.rotors.leftBackward[char]
        returnChar = self.rotors.middleBackward[returnChar]
        returnChar = self.rotors.rightBackward[returnChar]

        return returnChar