#!/usr/bin/python3

from config import Config
from enigma import Enigma

def main():
    Config.readKeys()

    enigma = Enigma(Config.setting('key1'), Config.setting('key2'), Config.setting('key3'))
    print('Enigma... Press Ctrl+D to stop')
    print('Commands:\n    encrypt <message>\n    decrypt <message>')

    try:
        while True:
            command = input('> ')
            try:
                spaceIndex = command.index(' ')
            except:
                print('Invalid command:')
                print('Commands:\n    encrypt <message>\n    decrypt <message>')
                continue

            if command[:spaceIndex] == 'encrypt':
                print(enigma.encrypt(command[spaceIndex+1:]))
            elif command[:spaceIndex] == 'decrypt':
                print(enigma.decrypt(command[spaceIndex+1:]))
            else:
                print('Invalid command')
                print('Commands:\n    encrypt <message>\n    decrypt <message>')           


    except (EOFError, KeyboardInterrupt):
        print() # Put the standard shell prompt on the next line




if __name__ == '__main__':
    main()