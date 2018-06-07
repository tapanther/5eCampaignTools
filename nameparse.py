import fileinput
import json


first = []
last = []

for line in fileinput.input():
    nameList = line.split()
    first.append(nameList[0])
    last.append(nameList[-1])

first = list(set(first))
last = list(set(last))

first.sort()
last.sort()

jsonOut = {"FirstNames" : first, "LastNames" : last}

with open('SafeholdFirstNames.json', 'w') as outfile:
    json.dump(jsonOut, outfile, indent=2)

