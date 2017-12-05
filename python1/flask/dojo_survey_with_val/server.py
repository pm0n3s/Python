from flask import Flask, render_template, request, url_for, flash, get_flashed_messages, redirect

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route ('/result',methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    
    if len(name) < 1 or len(comment) < 1:
        flash("input is required for name and comment")
        return redirect(url_for('index'))
    if len(comment) > 120:
        flash("comment can not be more than 120 characters")
        return redirect(url_for('index'))
    
    return render_template('result.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)