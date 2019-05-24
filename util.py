#!/usr/bin/python3

'''
    Cyclically rotates an array
'''
def rotate(collection, rotateAmount):
    if rotateAmount > 0:
        shift = rotateAmount % len(collection)
        collection = (collection[len(collection)-shift:] + collection[:len(collection)-shift])
        return collection
    else:
        shift = (-1*rotateAmount) % len(collection)
        collection = (collection[shift:] + collection[:shift])
        return collection
