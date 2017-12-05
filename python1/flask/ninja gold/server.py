from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "shhhh"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    if 'activity' not in session:
        session['activity'] = []
    activity = session['activity']
    
    if building == 'casino':
        gold = random.randint(-50, 50)
        if gold < 0:
            activity.append("Entered a " + building + " and lost " + str(gold) + " gold...Ouch..")
        else:
            activity.append("Entered a " + building + " and won " + str(gold) + " gold!")
    else:
        if building == 'farm':
            gold = random.randint(10, 20)      
        elif building == 'cave':
            gold = random.randint(5, 10)           
        elif building == 'house':
            gold = random.randint(2, 5) 
        activity.append("Earned " + str(gold) + " gold from " + building + "!")           
    
    session['gold'] = int(session['gold']) + gold
    session['activity'] = activity
    return redirect('/')

app.run(debug=True)