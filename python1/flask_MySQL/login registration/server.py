from flask import Flask, render_template, request, flash, get_flashed_messages, redirect, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

# app setup
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'loginreg')
app.secret_key = 'secrets'

# regex matches
NAME_VAL = re.compile(r'(^[a-zA-Z]{2,}$)')
EMAIL_VAL = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# index
@app.route('/')
def index():
    return render_template('index.html')

# successful 
@app.route('/success')
def success():
    if 'id' not in session:
        return redirect('/')
    query = 'SELECT * FROM users WHERE id = :id'
    data = {'id': session['id']}
    users = mysql.query_db(query, data)
    current_user = users[0]
    return render_template('success.html', user=current_user)

# register
@app.route('/register', methods=['POST'])
def register():
    errors = False

    # first name check
    if not re.match(NAME_VAL, request.form['first_name']):
        flash('First Name - letters only, at least 2 characters')
        errors = True

    # last name check
    if not re.match(NAME_VAL, request.form['last_name']):
        flash('Last Name - letters only, at least 2 characters')
        errors = True

    # email check
    if not re.match(EMAIL_VAL, request.form['email']):
        flash('Email - Valid Email format')
        errors = True

    # password check
    if len(request.form['pw']) < 8:
        flash('Password - at least 8 characters')
        errors = True

    # password confirmation check
    if request.form['pw'] != request.form['pwc']:
        flash('Password Confirmation - must match password')
        errors = True

    # errors check
    if errors:
        return redirect('/')
    # query block
    else:
        pw = request.form['pw']
        hashpw = bcrypt.generate_password_hash(pw)
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) \
                                VALUES (:firstn, :lastn, :email, :hashedpw, NOW(), NOW())'
        data = {
            'firstn': request.form['first_name'],
            'lastn': request.form['last_name'],
            'email': request.form['email'],
            'hashedpw': hashpw
        }
        user = mysql.query_db(query, data)
        # session check 
        if user is not 0:
            session['id'] = user
        else:
            flash('user creation failed')
        return redirect('/success')
# login
@app.route('/login', methods=['POST'])
def login():
    errors = False

    # email check
    if not re.match(EMAIL_VAL, request.form['email']):
        flash('Email - Valid Email format')
        errors = True

    # pw check
    if len(request.form['pw']) < 8:
        flash('Password - at least 8 characters')
        errors = True
    
    # error check
    if errors:
        return redirect('/')
    # querry block
    else:
        try:
            query = 'SELECT * FROM users WHERE email = :email'
            data = {
                'email': request.form['email']
            }
            user = mysql.query_db(query, data)
            hashedpw = user[0]['password']
            success = bcrypt.check_password_hash(hashedpw, request.form['pw'])
        except:
            flash('invalid email or password')
            return redirect('/')
    if success:
        session['id'] = user[0]['id']
        return redirect('/success')

app.run(debug=True)