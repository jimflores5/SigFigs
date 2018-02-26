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
    session.clear()
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
    if operation < 2:      #For + and -, create 2 values between 0.001 and 90 with 1 - 6 sig figs.
        sigFigs1 = random.randrange(1,7)
        power1 = random.randrange(-3,2)
        value1 = MakeNumber(sigFigs1,power1)
        sigFigs2 = random.randrange(1,7)
        power2 = random.randrange(-3,2)
        value2 = MakeNumber(sigFigs2,power2)
    else:                   #For * and /, create 2 values between 0.01 and 900 with 1 - 6 sig figs.
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

@app.route('/sftutorial1', methods=['POST', 'GET'])
def sftutorial1():
    if request.method == 'POST':
        displayText = int(request.form['displayText'])
        displayText += 1
    else:
        displayText=1
    
    return render_template('sftutorial1.html',title="Sig Fig Tutorial", page = 1, displayText=displayText)

@app.route('/sftutorial2', methods=['POST', 'GET'])
def sftutorial2():
    if request.method == 'POST':
        firstZeroRule = request.form['firstZeroRule']
        session['firstZeroRule'] = firstZeroRule
        secondHalf = True
        if firstZeroRule == '':
            flash('Please enter a response.', 'error')
            secondHalf = False
        
        return render_template('sftutorial2.html', answer = firstZeroRule, page = 2, secondHalf = secondHalf)

    return render_template('sftutorial2.html',title="Sig Fig Tutorial", page = 2, secondHalf=False)

@app.route('/sftutorial3', methods=['POST', 'GET'])
def sftutorial3():
    if request.method == 'POST':
        firstZeroRule = session.get('firstZeroRule', None)
        secondZeroRule = request.form['secondZeroRule']
        session['secondZeroRule'] = secondZeroRule
        secondHalf = True
        if secondZeroRule == '':
            flash('Please enter a response.', 'error')
            secondHalf = False
        
        return render_template('sftutorial3.html', firstZeroRule = firstZeroRule, secondZeroRule = secondZeroRule, page = 3, secondHalf = secondHalf)

    firstZeroRule = session.get('firstZeroRule', None)
    return render_template('sftutorial3.html',title="Sig Fig Tutorial", page = 3, firstZeroRule = firstZeroRule, secondHalf=False)

@app.route('/sftutorial4', methods=['POST', 'GET'])
def sftutorial4():
    firstZeroRule = session.get('firstZeroRule', None)
    secondZeroRule = session.get('secondZeroRule', None)
    return render_template('sftutorial4.html',title="Sig Fig Tutorial", page = 4, firstZeroRule=firstZeroRule, secondZeroRule=secondZeroRule)

@app.route('/sftutorial5', methods=['POST', 'GET'])
def sftutorial5():
    return render_template('sftutorial5.html',title="Sig Fig Tutorial", page = 5)

@app.route('/roundingtutorial1', methods=['POST', 'GET'])
def roundingtutorial1():
    return render_template('roundingtutorial1.html',title="Rounding Tutorial", page = 1)

@app.route('/roundingtutorial2', methods=['POST', 'GET'])
def roundingtutorial2():
    if request.method == 'POST':
        displayText = int(request.form['displayText'])
        displayText += 1
        roundedAnswer = request.form['5SigFigs']
        answers = []
        numCorrect = 0
        if displayText == 4 and roundedAnswer != '12.386':
            flash('Not quite correct.  Try again.', 'error')
            displayText = 3
        elif displayText>5:
            correctAnswers = ['0.00798','0.0080','0.008']
            for x in range(3):
                answers.append(request.form[str(3-x)+'SigFigs'])
                if CheckAnswer(correctAnswers[x],answers[x]):
                    flash('Correct!  :-)', 'correct')
                    numCorrect += 1
                else:
                    flash('Try again.', 'error')
    else:
        displayText=1
        roundedAnswer = ''
        answers = []
        numCorrect = 0

    return render_template('roundingtutorial2.html',title="Rounding Tutorial", page = 2, displayText=displayText, roundedAnswer = roundedAnswer, answers = answers, numCorrect = numCorrect)

@app.route('/roundingtutorial3', methods=['POST', 'GET'])
def roundingtutorial3():
    if request.method == 'POST':
        displayText = int(request.form['displayText'])
        displayText += 1
        example3 = request.form['example3']
        answers = []
        numCorrect = 0
        if displayText == 2 and example3 != '2380':
            flash('Not quite correct.  Try again.', 'error')
            displayText = 1
        elif displayText > 3:
            correctAnswers = ['0.0998','0.10','0.1']
            for x in range(3):
                answers.append(request.form[str(3-x)+'SigFigs'])
                if CheckAnswer(correctAnswers[x],answers[x]):
                    flash('Correct!  :-)', 'correct')
                    numCorrect += 1
                else:
                    flash('Try again.', 'error')
    else:
        displayText=1
        example3 = ''
        answers = []
        numCorrect = 0

    return render_template('roundingtutorial3.html',title="Rounding Tutorial", page = 3, displayText=displayText, answers = answers, example3 = example3, numCorrect = numCorrect)

@app.route('/roundingtutorial4', methods=['POST', 'GET'])
def roundingtutorial4():
    return render_template('roundingtutorial4.html',title="Rounding Tutorial", page = 4)

@app.route('/scinottutorial1', methods=['POST', 'GET'])
def scinottutorial1():
    if request.method == 'POST':
        displayText = int(request.form['displayText'])
        displayText += 1
        if displayText == 2:
            decimal = request.form['decimal']
            power = request.form['exponent']
            decimals = ['1.5', '15', '150', '1500']
            powers = ['3','2','1','0']
            if decimal in decimals:
                index = decimals.index(decimal)
                if power != powers[index]:
                    flash('Incorrect power.  Try again.', 'error')
                    displayText = 1
            else:
                flash('Incorrect decimal value.  Try again.', 'error')       
                displayText = 1
        else:
            decimal = ''
            power = ''
    else:
        displayText=1
        decimal = ''
        power = ''

    return render_template('scinottutorial1.html',title="Scientific Notation Tutorial", page = 1, displayText = displayText, decimal = decimal, exponent=power)

@app.route('/scinottutorial2', methods=['POST', 'GET'])
def scinottutorial2():
    if request.method == 'POST':
        #displayText = int(request.form['displayText'])
        #displayText += 1
        decimals = []
        powers = []
        exponents = []
        values = []
        sciValues = []
        for item in range(2):
            decimals.append(request.form['decimal'+str(item)])
            exponents.append(request.form['exponent'+str(item)])
            values.append(request.form['value'+str(item)])
            powers.append(request.form['power'+str(item)])
            sciValues.append(request.form['sciValue'+str(item)])
            if CheckAnswer(powers[item], exponents[item]) and CheckAnswer(sciValues[item],decimals[item]):
                flash('Correct!  :-)', 'correct')
            elif CheckAnswer(powers[item], exponents[item]) and not CheckAnswer(sciValues[item],decimals[item]):
                flash('Correct power.  Wrong decimal value.', 'error')
            elif CheckAnswer(sciValues[item],decimals[item]) and not CheckAnswer(powers[item], exponents[item]):
                flash('Correct decimal value.  Wrong power.', 'error')
            else:
                flash('Both entries are incorrect.  Try again.', 'error')

    else:
        values = []
        sciValues = []
        powers = []
        decimals = []
        exponents = []
        #displayText = 1
        for item in range(4):
            sigFigs = random.randrange(1,5)
            if item <= 1:
                power = random.randrange(0,7)
            else:
                power = random.randrange(-5,0)
            value = MakeNumber(sigFigs,power)
            values.append(value)
            powers.append(power)
            sciValues.append(ApplySciNotation(value, sigFigs))
        
    return render_template('scinottutorial2.html',title="Scientific Notation Tutorial", page = 2, values = values, decimals = decimals, exponents = exponents, sciValues = sciValues, powers = powers)

@app.route('/scinottutorial3', methods=['POST', 'GET'])
def scinottutorial3():
    sciValues = []
    powers = []
    for item in range(4):
        sigFigs = random.randrange(1,5)
        if item <= 1:
            power = random.randrange(0,7)
        else:
            power = random.randrange(-5,0)
        powers.append(power)
        sciValues.append(ApplySciNotation(MakeNumber(sigFigs,power), sigFigs))

    return render_template('scinottutorial3.html',title="Scientific Notation Tutorial", page = 3, sciValues = sciValues, powers = powers)

if __name__ == '__main__':
    app.run()