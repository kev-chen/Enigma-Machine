#!/usr/bin/python3

import json
import string

class Config:
    config = {
        'leftRotorRate': 5,
        'middleRotorRate': 7,
        'rightRotorRate': 1,
        'characters': dict(zip([ch for ch in string.ascii_uppercase] + [str(num) for num in range(10)], list(range(36)))), #A-Z0-9, indexed 0-35
        'key1': '',
        'key2': '',
        'key3': ''
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

