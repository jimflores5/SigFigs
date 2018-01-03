import random
from StringSigFigs import MakeNumber, RoundValue
from CalcsWithSigFigs import addValues, subtractValues, multiplyValues, divideValues, findDecimalPlaces

operators = ['+', '-', '*', '/']

def sfcalcs():
    operation = random.randrange(4) #Randomly select +, -, * or / using integers 0 - 3, respectively.
    if operation < 2:      #For for +, - or *, create 2 values between 0.001 and 90 with 1 - 6 sig figs.
        sigFigs1 = random.randrange(1,7)
        power1 = random.randrange(-3,2)
        value1 = MakeNumber(sigFigs1,power1)
        sigFigs2 = random.randrange(1,7)
        power2 = random.randrange(-3,2)
        value2 = MakeNumber(sigFigs2,power2)
    else:                   #For for /, create 2 values between 0.01 and 900 with 1 - 6 sig figs.
        sigFigs1 = random.randrange(1,7)
        power1 = random.randrange(-2,3)
        value1 = MakeNumber(sigFigs1,power1)
        sigFigs2 = random.randrange(1,7)
        power2 = random.randrange(-2,3)
        value2 = MakeNumber(sigFigs2,power2)

    if operation == 0:
        result = addValues(value1,value2)
        answer = input("{0} {1} {2} = ".format(value1,operators[operation],value2))
    elif operation == 1 and value1 > value2:
        result = subtractValues(value1,value2)
        answer = input("{0} {1} {2} = ".format(value1,operators[operation],value2))
    elif operation == 1 and value1 < value2:
        result = subtractValues(value2,value1)
        answer = input("{0} {1} {2} = ".format(value2,operators[operation],value1))
    elif operation == 2:
        result = multiplyValues(value1,sigFigs1,value2,sigFigs2)
        answer = input("{0} {1} {2} = ".format(value1,operators[operation],value2))
    elif float(value1)/float(value2)<1e-4:
        result = divideValues(value2,sigFigs2,value1,sigFigs1)
        answer = input("{0} {1} {2} = ".format(value2,operators[operation],value1))
    else:
        result = divideValues(value1,sigFigs1,value2,sigFigs2)
        answer = input("{0} {1} {2} = ".format(value1,operators[operation],value2))
    
    if answer == result:
        return "Correct!  :-)"
    else:
        return "Sorry, the correct answer is {0}".format(result)

for x in range(6):
    print("Complete the following calculation.  Round the answer to the proper number of significant figures.")
    feedback = sfcalcs()
    print(feedback)

"""
values = ["0.0173", "10.88", "1020","11.386","0.00137","303.2","0.22","0.88","0.0007","201"]

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

for x in range(len(values)-1):
    firstValue = random.choice(values)
    secondValue = random.choice(values)
    result = addValues(firstValue,secondValue)
    print("{0} + {1} = {2}".format(firstValue,secondValue,result))
    result = subtractValues(firstValue,secondValue)
    print("{0} - {1} = {2}".format(firstValue,secondValue,result))"""

