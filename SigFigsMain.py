import random
from flask import Flask, request, redirect, render_template, session, flash
import cgi
from StringSigFigs import MakeNumber, RoundValue
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
            return render_template('countingSigFigs.html', value=value, sigFigs = actualSigFigs, answer = answer)
        else:
            flash('Try again.', 'error')
            return render_template('countingSigFigs.html',value=value, sigFigs = actualSigFigs)

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
        if answer==roundedValue:
            flash('Correct!  :-)', 'correct')
            return render_template('roundingSigFigs.html', value=origValue, sigFigs = sigFigs, answer = answer)
        else:
            flash('Try again.', 'error')
            return render_template('roundingSigFigs.html',value=origValue, sigFigs = sigFigs, answer = answer)
    #TODO - Deal with placeholding zeros needing to be significant.  Add verification checks to prevent problematic numbers (e.g. 199) from being selected.
    sigFigs = random.randrange(1,7)
    power = random.randrange(-4,6)
    value = MakeNumber(9,power)
    return render_template('roundingSigFigs.html',title="Rounding Sig Figs", value=value, sigFigs = sigFigs)

@app.route('/sfcalcs', methods=['POST', 'GET'])
def sfcalcs():
    if request.method == 'POST':
        answer = request.form['answer']
        result = request.form['result']
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        if answer==result:
            flash('Correct!  :-)', 'correct')
            return render_template('sfCalcs.html',title="Calculations with Sig Figs", value1 = value1, value2 = value2, result = result, answer = answer, operation=operation)
        else:
            flash('Try again.', 'error')
            return render_template('sfCalcs.html',title="Calculations with Sig Figs", value1 = value1, value2 = value2, result = result, answer = answer, operation=operation)

    operators = ['+', '-', 'x', '/']
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

if __name__ == '__main__':
    app.run()