import random
from StringSigFigs import MakeNumber, RoundValue

operators = ['+','-','*','/']

def findDecimalPlaces(value):
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

def addWithPlaceholders(first,second):
    if float(first)>=1 and float(second)>=1:
        zeroCount = max(first.count("0"),second.count("0"))
    elif float(first)<1:
        zeroCount = second.count("0")
    else:
        zeroCount = first.count("0")
    temp1 = float(first)/10**zeroCount
    temp2 = float(second)/10**zeroCount
    print(first,second,zeroCount,temp1+temp2)
    result = str(int(round(temp1+temp2,0))*10**zeroCount)
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

def subtractWithPlaceholders(first,second):
    if float(first)>=1 and float(second)>=1:
        zeroCount = max(first.count("0"),second.count("0"))
    elif float(first)<1:
        zeroCount = second.count("0")
    else:
        zeroCount = first.count("0")
    temp1 = float(first)/10**zeroCount
    temp2 = float(second)/10**zeroCount
    result = str(int(round(temp1-temp2,0))*10**zeroCount)
    return result

def multiplyValues(value1, sf1, value2, sf2):
    sigFigs = min(sf1, sf2)
    product = str(float(value1)*float(value2))
    result = RoundValue(product, sigFigs)

    return result

def divideValues(value1, sf1, value2, sf2):
    sigFigs = min(sf1, sf2)
    quotient = str(float(value1)/float(value2))
    result = RoundValue(quotient, sigFigs)

    return result