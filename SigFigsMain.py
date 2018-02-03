import random
from flask import Flask, request, redirect, render_template, session, flash
import cgi
from StringSigFigs import MakeNumber, RoundValue, CheckAnswer, CheckRounding, ApplySciNotation
from CalcsWithSigFigs import addValues, subtractValues, multiplyValues, divideValues, findDecimalPlaces

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'yrtsimehc'

@app.route('/')
def index():
    return render_template('index.html',title="Sig Fig Practice")

@app.route('/countingsf', methods=['POST', 'GET'])
def countingsf():
    if request.method == 'POST':
        answer = request.form['answer']
        actualSigFigs = request.form['actualSigFigs']
        value = request.form['value']
        if answer==actualSigFigs:
            flash('Correct!  :-)', 'correct')
        else:
            flash('Try again, or click here to reveal the answer.', 'error')
        
        return render_template('countingSigFigs.html', value=value, sigFigs = actualSigFigs, answer = answer)

    sigFigs = random.randrange(1,7)
    power = random.randrange(-5,9)
    value = MakeNumber(sigFigs,power)
    return render_template('countingSigFigs.html',title="Counting Sig Figs", value=value, sigFigs = sigFigs)

@app.route('/roundingsf', methods=['POST', 'GET'])
def roundingsf():
    if request.method == 'POST':
        answer = request.form['answer']
        origValue = request.form['value']
        sigFigs = int(request.form['sigFigs'])
        roundedValue = RoundValue(origValue, sigFigs)
        if CheckAnswer(roundedValue, answer):
            flash('Correct!  :-)', 'correct')
        else:
            flash('Try again, or click here to reveal the answer.', 'error')
        
        return render_template('roundingSigFigs.html', value=origValue, sigFigs = sigFigs, answer = answer, roundedValue=roundedValue)
    
    iffyValue = True
    while iffyValue:
        sigFigs = random.randrange(1,7)
        power = random.randrange(-4,6)
        value = MakeNumber(9,power)
        result = RoundValue(value, sigFigs)
        iffyValue = CheckRounding(result,sigFigs)
    
    return render_template('roundingSigFigs.html',title="Rounding Sig Figs", value=value, sigFigs = sigFigs)

@app.route('/sfcalcs', methods=['POST', 'GET'])
def sfcalcs():
    #TODO - Deal with placeholding zeros needing to be significant.  Add scientific notation option?
    if request.method == 'POST':
        answer = request.form['answer']
        result = request.form['result']
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        if CheckAnswer(result, answer):
            flash('Correct!  :-)', 'correct')
        else:
            flash('Try again, or click here to reveal the answer.', 'error')
        
        return render_template('sfCalcs.html',title="Calculations with Sig Figs", value1 = value1, value2 = value2, result = result, answer = answer, operation=operation)

    operators = ['+', '-', 'x', '/']
    operation = random.randrange(4) #Randomly select +, -, * or / using integers 0 - 3, respectively.
    if operation <= 2:      #For +, - or *, create 2 values between 0.001 and 90 with 1 - 6 sig figs.
        sigFigs1 = random.randrange(1,7)
        power1 = random.randrange(-3,2)
        value1 = MakeNumber(sigFigs1,power1)
        sigFigs2 = random.randrange(1,7)
        power2 = random.randrange(-3,2)
        value2 = MakeNumber(sigFigs2,power2)
    else:                   #For /, create 2 values between 0.01 and 900 with 1 - 6 sig figs.
        sigFigs1 = random.randrange(1,7)
        power1 = random.randrange(-2,3)
        value1 = MakeNumber(sigFigs1,power1)
        sigFigs2 = random.randrange(1,7)
        power2 = random.randrange(-2,3)
        value2 = MakeNumber(sigFigs2,power2)

    if operation == 0:
        result = addValues(value1,value2)
        return render_template('sfCalcs.html',title="Calculations with Sig Figs", value1 = value1, value2 = value2, operation = operators[operation], result = result)
    elif operation == 1 and value1 > value2:
        result = subtractValues(value1,value2)
        return render_template('sfCalcs.html',title="Calculations with Sig Figs", value1 = value1, value2 = value2, operation = operators[operation], result = result)
    elif operation == 1 and value1 < value2:
        result = subtractValues(value2,value1)
        return render_template('sfCalcs.html',title="Calculations with Sig Figs", value1 = value2, value2 = value1, operation = operators[operation], result = result)
    elif operation == 2:
        result = multiplyValues(value1,sigFigs1,value2,sigFigs2)
        return render_template('sfCalcs.html',title="Calculations with Sig Figs", value1 = value1, value2 = value2, operation = operators[operation], result = result)
    elif float(value1)/float(value2)<1e-4:
        result = divideValues(value2,sigFigs2,value1,sigFigs1)
        return render_template('sfCalcs.html',title="Calculations with Sig Figs", value1 = value2, value2 = value1, operation = operators[operation], result = result)
    else:
        result = divideValues(value1,sigFigs1,value2,sigFigs2)
        return render_template('sfCalcs.html',title="Calculations with Sig Figs", value1 = value1, value2 = value2, operation = operators[operation], result = result)

@app.route('/scinotation', methods=['POST', 'GET'])
def scinotation():
    if request.method == 'POST':
        sciNot = request.form['sciNot']
        if sciNot=='True':              #Given a value in sci notation, the user eneters a number in standard notation.
            answer = request.form['answer']
            result = request.form['value']
            sciValue = request.form['sciValue']
            power = request.form['power']
            if CheckAnswer(result, answer):
                flash('Correct!  :-)', 'correct')
            else:
                flash('Try again, or click here to reveal the answer.', 'error')
            return render_template('scientificNotation.html',title="Scientific Notation", value = result, sciValue=sciValue, power = power, sciNot = True, answer = answer)
        else:                            #Given a value in standard notation, the user eneters a number in sci notation.
            answer = request.form['answer']
            result = request.form['value']
            sciValue = request.form['sciValue']
            power = request.form['power']
            exponent = request.form['exponent']
            if CheckAnswer(power, exponent) and CheckAnswer(sciValue,answer):
                flash('Correct!  :-)', 'correct')
            elif CheckAnswer(power, exponent) and not CheckAnswer(sciValue,answer):
                flash('Correct power.  Wrong decimal value.', 'error')
            elif CheckAnswer(sciValue,answer) and not CheckAnswer(power, exponent):
                flash('Correct decimal value.  Wrong power.', 'error')
            else:
                flash('Both entries are incorrect.  Try again, or click to reveal the answer.', 'error')
                
            return render_template('scientificNotation.html',title="Scientific Notation", value = result, sciValue=sciValue, power = power, sciNot = False, answer = answer, exponent = exponent)

    sigFigs = random.randrange(1,5)
    power = random.randrange(-5,9)
    value = MakeNumber(sigFigs,power)
    sciValue = ApplySciNotation(value, sigFigs)
    if random.randrange(2) == 0:  #Flip a coin: If '0', ask the user to change sci notation into standard notation.
        return render_template('scientificNotation.html',title="Scientific Notation", value = value, sciValue=sciValue, power = power, sciNot = True)
    else:                         #Otherwise ('1'), ask the user to change standard notation into sci notation.
        return render_template('scientificNotation.html',title="Scientific Notation", value=value, sciValue=sciValue, power = power, sciNot = False)

@app.route('/sftutorial1')
def sftutorial1():
    return render_template('sftutorial1.html',title="Sig Fig Tutorial", page = 1)

@app.route('/sftutorial2')
def sftutorial2():
    return render_template('sftutorial2.html',title="Sig Fig Tutorial", page = 2)

if __name__ == '__main__':
    app.run()