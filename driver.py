#!/usr/bin/python3

import sys
from enigma import Enigma

def main():
    try:
        key1 = sys.argv[1]
        key2 = sys.argv[2]
    except KeyError as e:
        key1 = input('key1=')
        key2 = input('key2=')

    enigma = Enigma(key1, key2)
    print('Enigma. Press Ctrl+D to stop.')
    while True:
        command = input('> ')
        spaceIndex = command.index(' ')

        if command[:spaceIndex] == 'encrypt':
            print(enigma.encrypt(command[spaceIndex+1:]))
        elif command[:spaceIndex] == 'decrypt':
            print(enigma.decrypt(command[spaceIndex+1:]))




if __name__ == '__main__':
    main()