import random
from StringSigFigs import Number, MakeNumber, RoundValue, CheckAnswer
from CalcsWithSigFigs import subtractValues, multiplyValues, divideValues, findDecimalPlaces

operators = ['+', '-', '*', '/']

def addValues(first,second):
    firstDP = findDecimalPlaces(first.value)
    secondDP = findDecimalPlaces(second.value)
    if firstDP == 0 or secondDP == 0:
        result = str(int(round((float(first.value)+float(second.value)),0)))
        return result
    elif firstDP > secondDP:
        result = str(round(float(first.value)+float(second.value),secondDP))
        resultDP = findDecimalPlaces(result)
        if resultDP < secondDP:
            result += "0"
    else:
        result = str(round(float(first.value)+float(second.value),firstDP))
        resultDP = findDecimalPlaces(result)
        if resultDP < firstDP:
            result += "0"
    return result

def subtractValues(first,second):
    firstDP = findDecimalPlaces(first.value)
    secondDP = findDecimalPlaces(second.value)
    if firstDP == 0 or secondDP == 0:
        result = str(int(round((float(first.value)-float(second.value)),0)))
        return result
    elif firstDP > secondDP:
        result = str(round(float(first.value)-float(second.value),secondDP))
        resultDP = findDecimalPlaces(result)
        if resultDP < secondDP:
            result += "0"
    else:
        result = str(round(float(first.value)-float(second.value),firstDP))
        resultDP = findDecimalPlaces(result)
        if resultDP < firstDP:
            result += "0"*(firstDP-resultDP)
    return result

def multiplyValues(value1, value2):
    sigFigs = min(value1.sigFigs, value2.sigFigs)
    product = str(float(value1.value)*float(value2.value))
    result = RoundValue(product, sigFigs)

    return result

def divideValues(value1, value2):
    sigFigs = min(value1.sigFigs, value2.sigFigs)
    quotient = str(float(value1.value)/float(value2.value))
    result = RoundValue(quotient, sigFigs)

    return result

def sfcalcs(value1, value2, operation):
    if operation == 0:
        result = addValues(value1,value2)
        answer = input("{0} {1} {2} = ".format(value1.value,operators[operation],value2.value))
    elif operation == 1 and value1.value > value2.value:
        result = subtractValues(value1,value2)
        answer = input("{0} {1} {2} = ".format(value1.value,operators[operation],value2.value))
    elif operation == 1 and value1.value < value2.value:
        result = subtractValues(value2,value1)
        answer = input("{0} {1} {2} = ".format(value2.value,operators[operation],value1.value))
    elif operation == 2:
        result = multiplyValues(value1,value2)
        answer = input("{0} {1} {2} = ".format(value1.value,operators[operation],value2.value))
    elif float(value1.value)/float(value2.value)<1e-4:
        result = divideValues(value2,value1)
        answer = input("{0} {1} {2} = ".format(value2.value,operators[operation],value1.value))
    else:
        result = divideValues(value1,value2)
        answer = input("{0} {1} {2} = ".format(value1.value,operators[operation],value2.value))

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

def ApplySciNotation(result):
    if result.value[0] == "0":
        for x in range(2, len(result.value)):
            if result.value[x] != "0":
                startHere = x
                if result.sigFigs > 1:
                    sciNot = result.value[x]+"."
                else:
                    sciNot = result.value[x]
                break
        for digit in range(startHere+1,len(result.value)):
            sciNot += result.value[digit]
        sciNot += "x10^-{0}".format(startHere-1)
    elif result.value.find(".") >= 0:
        decimalIndex = result.value.find(".")
        sciNot = result.value[0]+"."
        for x in range(1,result.sigFigs+1):
            if result.value[x] != ".":
                sciNot += result.value[x]
        sciNot += "x10^{0}".format(decimalIndex-1)
    else:
        sciNot = result.value[0]
        if result.sigFigs > 1:
            sciNot += "."        
        for x in range(1,sigFigs):
            sciNot += result.value[x]
        sciNot += "x10^{0}".format(len(result.value)-1)
    return sciNot

for x in range(6):
    operation = random.randrange(4) #Randomly select +, -, * or / using integers 0 - 3, respectively.
    if operation <= 2:      #For for +, - or *, create 2 values between 0.001 and 90 with 1 - 6 sig figs.
        value1 = Number(random.randrange(1,7),random.randrange(-3,2))
        value2 = Number(random.randrange(1,7),random.randrange(-3,2))
    else:                   #For for /, create 2 values between 0.01 and 900 with 1 - 6 sig figs.
        value1 = Number(random.randrange(1,7),random.randrange(-2,3))
        value2 = Number(random.randrange(1,7),random.randrange(-2,3))

    result = sfcalcs(value1, value2, operation)
    print(result)

#TODO - 1) Add interactive tutorial pages.  Perhaps with short videos?
#       2) Develop measurement practice (interactive).
#       3) Create a Number class and refactor sig fig code to use it instead of separate value, sigFig & power variables.
#       4) Ignore #3.  Using the Number class did not actually streamline the code much at all.
#       5) For the sig fig practice pages, add an option for 'See correct answer'.  It should appear when the user submits an incorrect response.