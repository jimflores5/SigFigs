import random

def MakeNumber(sigFigs, power):
    allDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    firstDigit = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    if power < 0:
        value = "0."+ -(power+1)*"0" + random.choice(firstDigit)
        for digit in range(sigFigs-1):
            value += random.choice(allDigits)
    
        return value
    elif sigFigs - power < 2:
        value = random.choice(firstDigit)

        for digit in range(sigFigs-1):
            if digit == sigFigs-2:
                value += random.choice(firstDigit)
            else:
                value += random.choice(allDigits)
                
        value += (power-sigFigs+1)*"0"

        return value
    else:
        value = random.choice(firstDigit)
        decimalLocation = power +1
        for digit in range(1, sigFigs+1):
            if digit == decimalLocation:
                value += "."
            else:
                value += random.choice(allDigits)
        return value

def RoundValue(value, sigFigs):        
    decimalIndex = value.find('.')
    if decimalIndex < 0:
        decimalIndex = len(value)

    if float(value)<1:
        placeholders = 0
        for x in range(2,len(value)):
            if value[x] == "0":
                placeholders += 1
            else:
                break

        roundToSigFigs = round(float(value)*10**placeholders,sigFigs)
        addPlaceholders = round(roundToSigFigs/10**placeholders,sigFigs+placeholders)

        if len(str(roundToSigFigs))-sigFigs < 3:
            result = str(addPlaceholders)+"0"*(2-(len(str(roundToSigFigs))-sigFigs))
        else:
            result = str(addPlaceholders)
        return result
    else:
        roundToSigFigs = round(float(value)/10**decimalIndex,sigFigs)
        addZeros = round(roundToSigFigs*10**decimalIndex,sigFigs-decimalIndex)

        if sigFigs <= decimalIndex:
            result = str(int(addZeros))
        elif len(str(addZeros))-sigFigs <= 0:
            result = str(addZeros)+"0"*(sigFigs-len(str(addZeros))+1)
        else:
            result = str(addZeros)

        return result

def CheckAnswer(result, answer):
    if answer == '':        #Check for null result.
        return False

    if answer[0] == ".":    #Convert '.xx' to '0.xx'.
        answer = "0"+answer

    if result == answer:    #Check for exact result.
        return True
    else:
        return False

def CheckRounding(result, sigFigs):
    if float(result)>=10 and sigFigs <= len(result):
        if result[sigFigs-1] == "0" and result.find('.') == -1:
            return True
        else:
            return False

def Main():
    for x in range(4):
        sigFigs = random.randrange(1,7)
        power = random.randrange(-5,9)
        value = MakeNumber(sigFigs,power)
        text = "How many sig figs are in the value: "+ str(value)+"?\n"
        answer = int(input(text))
        if answer == sigFigs:
            print("Correct!")
        else:
            print("Sorry,",value,"has",sigFigs,"sig figs.")