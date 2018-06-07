#!/usr/local/bin/python3.6

import json
import sys
import random

def generateNames():
    '''
    Reads a supplied JSON file containing two arrays, one with first
    names and one with last names, then randomly creates a set of names.
    '''

    filename = sys.argv[-1]

    nameDict = {}
    with open(filename, 'r') as jsonData:
        nameDict = json.load(jsonData)
    
    firstNames = nameDict["FirstNames"]
    maleFirstNames = firstNames["Male"]
    femaleFirstNames = firstNames["Female"]
    lastNames = nameDict["LastNames"]

    print("Male:")
    for i in range(10):
        first = random.choice(maleFirstNames)
        last = random.choice(lastNames)
        print("{} {}".format(first, last))

    print("\nFemale:")
    for i in range(10):
        first = random.choice(femaleFirstNames)
        last = random.choice(lastNames)
        print("{} {}".format(first, last))

        

if __name__ == "__main__":
    generateNames()
