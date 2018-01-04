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
            print("Rounding {0} to {1} sig figs is ambiguous.  Choosing a new number...".format(result,sigFigs))
            return True
        else:
            return False

#TODO - Deal with placeholding zeros needing to be significant.  Add verification checks to prevent problematic numbers (e.g. 199) from being selected.
values = ['199', '19.61824', '219.7', '1.95', '11.96', '1999', '2818.05']
sfs = [1, 2, 3, 4, 6]
for x in range(6):
    iffyValue = True
    while iffyValue:
        sigFigs = random.choice(sfs)
        power = random.randrange(-4,6)
        value = random.choice(values)
        result = RoundValue(value, sigFigs)
        iffyValue = CheckRounding(result,sigFigs)

    answer = input("Round {0} to {1} significant figures: ".format(value, sigFigs))

    if CheckAnswer(result, answer):
        print("Correct!  :-)")
    else:
        print("Sorry, the correct answer is {0}.".format(result))
