import random
from StringSigFigs import MakeNumber

operators = ['+','-','*','/']

for y in range(5):
    numbers = dict()
    for x in range(2):
        sigFigs = random.randrange(1,6)
        power = random.randrange(-3,4)
        value = MakeNumber(sigFigs,power)
        numbers[sigFigs] = value
    op = random.randrange(0,4)
    print(list(numbers.values())[0],operators[op],list(numbers.values())[1])
    result = float(list(numbers.values())[0]) - float(list(numbers.values())[1])
    print(result)
    
