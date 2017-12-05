from flask import Flask, render_template, session, url_for, request, redirect, flash, get_flashed_messages
import random

app = Flask(__name__)
app.secret_key = 'secretkeyissecret'

#not the best way but this makes a list of set_answers. 
# sets the index[0] as the session['answer'] then when the number
# is found the reset pops the whole list. no time to optimize atm

# should add an if session not set set = randint
# on reset pop the session

@app.route('/')
def index():
    if 'answer' not in session:
        session['answer'] = random.randint(1, 100)
    # print session['answer']
    return render_template('index.html')

@app.route('/high')
def high():
    flash("Too high")
    return redirect(url_for('index'))

@app.route('/low')
def low():
    flash("Too low")
    return redirect(url_for('index'))

@app.route('/equal')
def equal():
    return render_template('playagain.html')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('answer')
    return redirect(url_for('index'))

@app.route('/evaluate', methods=['POST'])
def eval():
    session['guess'] = request.form['guess']
    # print session['answer']
    # print session['guess']

    if int(session['guess']) > int(session['answer']):
        return redirect(url_for('high'))
    elif int(session['guess']) < int(session['answer']):
        return redirect(url_for('low'))
    else:
        return redirect(url_for('equal'))
    return redirect(url_for('index'))

app.run(debug=True)