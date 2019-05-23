#!/usr/bin/python3

class Config:
    config = {
        'leftRotorRate': 5,
        'middleRotorRate': 7,
        'rightRotorRate': 1
    }

    @staticmethod
    def setting(value):
        if value not in Config.config:
            return None
        return Config.config[value]
