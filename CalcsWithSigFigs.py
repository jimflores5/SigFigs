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
    
for trials in range(5):
    operation = random.randrange(4)
    if operation <= 2:
        sigFigs1 = random.randrange(1,7)
        power1 = random.randrange(-3,2)
        value1 = MakeNumber(sigFigs1,power1)
        sigFigs2 = random.randrange(1,7)
        power2 = random.randrange(-3,2)
        value2 = MakeNumber(sigFigs2,power2)
    else:
        sigFigs1 = random.randrange(1,7)
        power1 = random.randrange(-2,3)
        value1 = MakeNumber(sigFigs1,power1)
        sigFigs2 = random.randrange(1,7)
        power2 = random.randrange(-2,3)
        value2 = MakeNumber(sigFigs2,power2)

    if operation == 0:
        result = addValues(value1,value2)
        print("{0} {1} {2} = {3}".format(value1,operators[operation],value2, result),"\n")
    elif operation == 1:
        result = subtractValues(value1,value2)
        print("{0} {1} {2} = {3}".format(value1,operators[operation],value2, result),"\n")
    elif operation == 2:
        result = multiplyValues(value1,sigFigs1,value2,sigFigs2)
        print("{0} {1} {2} = {3}".format(value1,operators[operation],value2, result),"\n")
    elif float(value1)/float(value2)<1e-4:
        result = divideValues(value2,sigFigs2,value1,sigFigs1)
        print("{0} {1} {2} = {3}".format(value2,operators[operation],value1, result),"\n")
    else:
        result = divideValues(value1,sigFigs1,value2,sigFigs2)
        print("{0} {1} {2} = {3}".format(value1,operators[operation],value2, result),"\n")
