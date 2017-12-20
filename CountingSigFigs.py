import random

for x in range(1,6):
    sigFigs = random.randrange(1,7)
    power = random.randrange(-4,5)
    value = round(random.random(),sigFigs)
    result = round(value*10**power,sigFigs-power)
    print(value, power, result)

print()

for y in range(1,5):
    sigFigs = random.randrange(1,3)
    if sigFigs == 1:
        value = random.randrange(1,9)
        power = random.randrange(-4,5)
        print(value, power, value*10**power)
    else:
        value = random.randrange(10,100)
        if value%10 == 0:
            power = random.randrange(-5,1)
        else:
            power = random.randrange(-4,7)
        print(value, power, value*10**power)