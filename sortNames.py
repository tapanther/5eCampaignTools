#!/usr/local/bin/python3.6

import json
import sys
import random


def sortNames():

    filename = sys.argv[-1]

    nameDict = {}
    with open(filename, 'r') as jsonData:
        nameDict = json.load(jsonData)
    
    firstNames = nameDict["FirstNames"]
    lastNames = nameDict["LastNames"]

    male = []
    female = []
    unknown = []
    
    for name in firstNames:
        gender = input("{} : ".format(name))
        if gender == "m":
            male.append(name)
        elif gender == "f":
            female.append(name)
        else:
            unknown.append(name)

    jsonOut = {"FirstNames" : {"Male" : male, "Female" : female}, "LastNames" : lastNames, "Unknown" : unknown}

    with open('names.json', 'w') as outfile:
        json.dump(jsonOut, outfile, indent=2)


if __name__ == "__main__":
    sortNames()
