from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "aVerySecretSecret"
mysql = MySQLConnector(app, 'create_email_validation')
EMAIL_VAL = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    if re.match(EMAIL_VAL, request.form['email']):
        query = 'INSERT INTO users (email, created_at) VALUES ("{}", NOW());'.format(request.form['email'])
        mysql.query_db(query)
        flash('The email address you entered is a VALID email address! Thank you!')
        return redirect('/success')
    else:
        flash('Email is not valid!')
        return redirect('/')

@app.route('/success')
def success():
    query = mysql.query_db('SELECT email, DATE_FORMAT(created_at, "%m/%d/%y %h:%i %p") AS created FROM users;')
    return render_template('success.html', users = query)

app.run(debug=True)