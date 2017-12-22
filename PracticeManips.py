import random
from StringSigFigs import MakeNumber, RoundValue
from CalcsWithSigFigs import addValues, subtractValues, multiplyValues, divideValues, findDecimalPlaces

values = ["0.0173", "10.88", "1020","11.386","0.00137","303.2","0.22","0.88","0.0007","201"]

"""def findDecimalPlaces(value):
    decimalIndex = value.find(".")
    if decimalIndex>0:
        decimalPlaces = len(value)-decimalIndex-1
    else:
        decimalPlaces = 0
    return decimalPlaces

def addValues(first,second):
    firstDP = findDecimalPlaces(first)
    secondDP = findDecimalPlaces(second)
    if firstDP == 0 or secondDP == 0:
        result = str(int(round((float(first)+float(second)),0)))
        return result
    elif firstDP > secondDP:
        result = str(round(float(first)+float(second),secondDP))
        resultDP = findDecimalPlaces(result)
        if resultDP < secondDP:
            result += "0"
    else:
        result = str(round(float(first)+float(second),firstDP))
        resultDP = findDecimalPlaces(result)
        if resultDP < firstDP:
            result += "0"
    return result

def subtractValues(first,second):
    firstDP = findDecimalPlaces(first)
    secondDP = findDecimalPlaces(second)
    if firstDP == 0 or secondDP == 0:
        result = str(int(round((float(first)-float(second)),0)))
        return result
    elif firstDP > secondDP:
        result = str(round(float(first)-float(second),secondDP))
        resultDP = findDecimalPlaces(result)
        if resultDP < secondDP:
            result += "0"
    else:
        result = str(round(float(first)-float(second),firstDP))
        resultDP = findDecimalPlaces(result)
        if resultDP < firstDP:
            result += "0"*(firstDP-resultDP)
    return result

for x in range(len(values)-1):
    firstValue = random.choice(values)
    secondValue = random.choice(values)
    result = addValues(firstValue,secondValue)
    print("{0} + {1} = {2}".format(firstValue,secondValue,result))
    result = subtractValues(firstValue,secondValue)
    print("{0} - {1} = {2}".format(firstValue,secondValue,result))"""

