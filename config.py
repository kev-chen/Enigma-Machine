#!/usr/bin/python3

import json
import string

class Config:
    config = {
        'leftRotorRate': 5,
        'middleRotorRate': 7,
        'rightRotorRate': 1,
        'characters': dict(zip([ch for ch in string.ascii_uppercase] + [str(num) for num in range(10)], list(range(36)))), # A-Z0-9, indexed 0-35
        'leftRotor': ['2','y','z','0','1','a','w','i','p','k','s','n','3','t','e','r','m','u','c','5','v','6','x','7','f','q','o','l','4','8','g','d','9','b','j','h'],
        'middleRotor': ['0','l','x','1','2','8','h','b','3','n','r','o','k','d','t','7','c','6','p','i','v','j','4','a','u','w','m','e','9','5','q','s','z','g','y','f'],
        'rightRotor': ['3','5','h','e','f','g','d','q','8','m','2','k','l','j','n','s','u','w','o','v','r','x','z','c','i','9','t','7','b','p','a','0','1','y','6','4'],
        'key1': '', # For plugboard
        'key2': '', # For reflector
        'key3': ''  # For initial wheel rotations
    }

    @staticmethod
    def setting(value):
        if value not in Config.config:
            return None
        return Config.config[value]

    @staticmethod
    def readKeys():
        try:
            with open('keys.json', 'r') as jsonFile:
                data = json.load(jsonFile)
                Config.config['key1'] = data['key1']
                Config.config['key2'] = data['key2']
                Config.config['key3'] = data['key3']
        except Exception as e:
            print(f"Error retrieving keys: {str(e)}")
            quit()

