#Create a simple web application that holds a counter that 
# increments every time the page is visited. Complete this using 
# session.

from flask import Flask, render_template, redirect, session, request,url_for

app = Flask(__name__)
app.secret_key = 'secrets_secrets_are_no_fun'
counter = [0]
@app.route('/')
def index():
    counter[0] += 1
    session['counter'] = counter
    return render_template('index.html', counter=session['counter'])

@app.route('/ninja')
def ninja():
    counter[0] += 1
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    counter[0] = 0
    return redirect(url_for('index'))

app.run(debug=True)