import random
from StringSigFigs import MakeNumber, RoundValue, CheckAnswer
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

    if CheckAnswer(result, answer):
        return "Correct!  :-)"
    else:
        return "Sorry, the correct answer is {0}".format(result)

def CheckRounding(result, sigFigs):
    if float(result)>=10 and sigFigs <= len(result):
        if result[sigFigs-1] == "0" and result.find('.') == -1:
            print("Rounding {0} to {1} sig figs is ambiguous.  Changing to scientific notation...".format(result,sigFigs))
            return True
        else:
            return False

def ApplySciNotation(result, sigFigs):
    if result[0] == "0":
        for x in range(2, len(result)):
            if result[x] != "0":
                startHere = x
                if sigFigs > 1:
                    sciNot = result[x]+"."
                else:
                    sciNot = result[x]
                break
        for digit in range(startHere+1,len(result)):
            sciNot += result[digit]
        sciNot += "x10^-{0}".format(startHere-1)
    elif result.find(".") >= 0:
        decimalIndex = result.find(".")
        sciNot = result[0]+"."
        for x in range(1,sigFigs+1):
            if result[x] != ".":
                sciNot += result[x]
        sciNot += "x10^{0}".format(decimalIndex-1)
    else:
        sciNot = result[0]
        if sigFigs > 1:
            sciNot += "."        
        for x in range(1,sigFigs):
            sciNot += result[x]
        sciNot += "x10^{0}".format(len(result)-1)
    return sciNot

for x in range(6):
    sigFigs = random.randrange(1,7)
    power = random.randrange(-5,9)
    value = MakeNumber(sigFigs,power)
    result = ApplySciNotation(value,sigFigs)
    print(value,"=",result)

"""#TODO - Deal with placeholding zeros needing to be significant.  Use scientific notation.
values = ['199', '2.0', '324.7', '1.00', '11.96', '1999', '12.0']
sfs = [3, 2, 4, 3, 4, 4, 3]

for x in range(6):
    operation = random.randrange(2,4)
    choice1 = random.randrange(7)
    sigFigs1 = sfs[choice1]
    value1 = values[choice1]

    choice2 = random.randrange(7)
    sigFigs2 = sfs[choice2]
    value2 = values[choice2]

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
        if CheckRounding(result, min(sigFigs1,sigFigs2)):
            result = ApplySciNotation(result, min(sigFigs1,sigFigs2))
        answer = input("{0} {1} {2} = ".format(value1,operators[operation],value2))
    elif float(value1)/float(value2)<1e-4:
        result = divideValues(value2,sigFigs2,value1,sigFigs1)
        if CheckRounding(result, min(sigFigs1,sigFigs2)):
            result = ApplySciNotation(result, min(sigFigs1,sigFigs2))
        answer = input("{0} {1} {2} = ".format(value2,operators[operation],value1))
    else:
        result = divideValues(value1,sigFigs1,value2,sigFigs2)
        if CheckRounding(result, min(sigFigs1,sigFigs2)):
            result = ApplySciNotation(result, min(sigFigs1,sigFigs2))
        answer = input("{0} {1} {2} = ".format(value1,operators[operation],value2))

    if CheckAnswer(result, answer):
        print("Correct!  :-)")
    else:
        print("Sorry, the correct answer is {0}.".format(result))"""
