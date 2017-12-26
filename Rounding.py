import random

values = ['123.45', '0.0140', '9876', '9.0385', '103', '0.02', '0.01899', '0.80']
valueSigFigs = [5, 3, 4, 5, 3, 1, 4, 2]

def multiplyValues(value1, sf1, value2, sf2):
    sigFigs = min(sf1, sf2)
    product = str(float(value1)*float(value2))
    answer = roundValue(product, sigFigs)

    return answer

def divideValues(value1, sf1, value2, sf2):
    sigFigs = min(sf1, sf2)
    quotient = str(float(value1)/float(value2))
    answer = roundValue(quotient, sigFigs)

    return answer

def roundValue(value, sigFigs):        
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

"""for x in range(5):
    index1 = random.randrange(len(values))
    index2 = random.randrange(len(values))
    value1 = values[index1]
    sf1 = valueSigFigs[index1]
    value2 = values[index2]
    sf2 = valueSigFigs[index2]

    product = multiplyValues(value1,sf1,value2,sf2)
    if float(value1)/float(value2)<1e-4:
        quotient = divideValues(value2,sf2,value1,sf1)
        print(value1,"*",value2,"=",product)
        print(value2,"/",value1,"=",quotient,"\n")
    else:
        quotient = divideValues(value1,sf1,value2,sf2)
        print(value1,"*",value2,"=",product)
        print(value1,"/",value2,"=",quotient,"\n")"""
    
