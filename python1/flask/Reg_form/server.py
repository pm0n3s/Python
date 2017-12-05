from flask import Flask, render_template, redirect, request, session, flash, get_flashed_messages
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PW_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d).+$')

app = Flask(__name__)
app.secret_key = "ItsASecretShhh"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']
# True var block
    email = True
    text = True
    numbers = True
    ispass = True
    passlen = True
    confmat = True
# email block
    if not EMAIL_REGEX.match(request.form['email']):
        if len(session['email']) < 1:
            flash('email is required')
            text = False
        else:
            flash("invalid email address")
            email = False
# first name block
    if not session['first_name'].isalpha():
        if len(session['first_name']) < 1:
            flash('first name required')
            text = False
        else:
            flash('first name can not contain numbers')
            numbers = False
# last name block
    if not session['last_name'].isalpha():
        if len(session['last_name']) < 1:
            flash('last name required')
            text = False
        else:
            flash('last name can not contain numbers')
            numbers = False
# password block
    if not PW_REGEX.match(request.form['password']):
        flash('password must contain at least 1 uppercase and 1 number')
    elif len(session['password']) < 9:
        if len(session['password']) < 1:
            flash('password required')
            text = False
        else:
            flash('password must be more than 8 characters')
            passlen = False
# confirm password block
    if session['confirm_password'] != session['password']:
        if len(session['confirm_password']) < 1:
            flash('confirm password required')
            text = False
        else:
            flash('confirm password does not match password')

# main logic block
    if email and text and numbers and ispass and passlen and confmat:
        flash('Thanks for submitting your information')
    else:
        flash('please fix errors and resubmit')

    return redirect('/')

app.run(debug=True)


'''
All fields are required and must not be blank - DONE
First and Last Name cannot contain any numbers - DONE
Password should be more than 8 characters - DONE
Email should be a valid email - DONE
Password and Password Confirmation should match - DONE
If the form with all the information is submitted properly, simply have it say 
a message "Thanks for submitting your information." - DONE

When the form is submitted, make sure the user submits appropriate information. 
If the user did not submit appropriate information, return the error(s) above 
the form that asks the user to correct the information.

Ninja Version:
Add the validation that requires a password to have at least 1 uppercase letter 
and 1 numeric value. - DONE
Hacker Version:
Add a birth-date field that must be validated as a valid date (and must be from 
the past). - possibly in the future'''