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

if __name__ == '__main__':
    app.run()

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

