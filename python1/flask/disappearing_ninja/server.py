from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def showall():
    colorone = url_for('static', filename='Ninjas/leonardo.jpg')
    colortwo = url_for('static', filename='Ninjas/michelangelo.jpg')
    colorthree = url_for('static', filename='Ninjas/raphael.jpg')
    colorfour = url_for('static', filename='Ninjas/donatello.jpg')
    return render_template('ninja.html', colorone=colorone, colortwo=colortwo, colorthree=colorthree, colorfour=colorfour)

@app.route('/ninja/<color>')
def show_user_profile(color):
    if len(color) < 1:
        colorone = url_for('static', filename='Ninjas/leonardo.jpg')
        colortwo = url_for('static', filename='Ninjas/michelangelo.jpg')
        colorthree = url_for('static', filename='Ninjas/raphael.jpg')
        colorfour = url_for('static', filename='Ninjas/donatello.jpg')
    if color.lower() == 'blue':
        colorone = url_for('static', filename='Ninjas/leonardo.jpg')
        colortwo = url_for('static', filename='Ninjas/leonardo.jpg')
        colorthree = url_for('static', filename='Ninjas/leonardo.jpg')
        colorfour = url_for('static', filename='Ninjas/leonardo.jpg')
    elif color.lower() == 'orange':
        colorone = url_for('static', filename='Ninjas/michelangelo.jpg')
        colortwo = url_for('static', filename='Ninjas/michelangelo.jpg')
        colorthree = url_for('static', filename='Ninjas/michelangelo.jpg')
        colorfour = url_for('static', filename='Ninjas/michelangelo.jpg')
    elif color.lower() == 'red':
        colorone = url_for('static', filename='Ninjas/raphael.jpg')
        colortwo = url_for('static', filename='Ninjas/raphael.jpg')
        colorthree = url_for('static', filename='Ninjas/raphael.jpg')
        colorfour = url_for('static', filename='Ninjas/raphael.jpg')
    elif color.lower() == 'purple':
        colorone = url_for('static', filename='Ninjas/donatello.jpg')
        colortwo = url_for('static', filename='Ninjas/donatello.jpg')
        colorthree = url_for('static', filename='Ninjas/donatello.jpg')
        colorfour = url_for('static', filename='Ninjas/donatello.jpg')
    else:
        colorone = url_for('static', filename='Ninjas/notapril.jpg')
        colortwo = url_for('static', filename='Ninjas/notapril.jpg')
        colorthree = url_for('static', filename='Ninjas/notapril.jpg')
        colorfour = url_for('static', filename='Ninjas/notapril.jpg')

    return render_template("ninja.html", colorone=colorone, colortwo=colortwo, colorthree=colorthree, colorfour=colorfour)

app.run(debug=True)