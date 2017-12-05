from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "aVerySecretSecret"
mysql = MySQLConnector(app, "mydb")

#READ
@app.route('/')
def index():
    query = mysql.query_db('SELECT * FROM users;')
    return render_template('index.html', users = query)
#CREATE
@app.route('/friends', methods=['POST'])
def add_friend():
    query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) \
                            VALUES (:firstname, :lastname, :email, NOW(), NOW())'
    data = {
        'firstname': request.form['first_name'],
        'lastname': request.form['last_name'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/')
#DELETE
@app.route('/friends/<id>/delete', methods=['POST'])
def delete_user(id):
    query = 'DELETE FROM users WHERE id = :id'
    data = {
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')
#UPDATE
@app.route('/friends/<id>/edit')
def edit(id):
    query = 'SELECT * FROM users WHERE id = :id'
    data = {
        'id': id
    }
    info = mysql.query_db(query, data)
    return render_template('edit.html', users = info[0])

@app.route('/friends/<id>', methods=['POST'])
def edited(id):
    query = 'UPDATE users SET first_name = :firstname, last_name = :lastname, \
                            email = :email, updated_at = NOW() WHERE id = :id'
    data = {
        'firstname': request.form['first_name'],
        'lastname': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)