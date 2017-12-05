from django.shortcuts import render, redirect
from datetime import datetime
from time import strftime, gmtime

# Create your views here.
def index(request):
    if "words" not in request.session:
        request.session['words'] = []
        return render(request, "words/index.html")
    else:
        context = {
            "words": request.session["words"]
        }
        return render(request, "words/index.html", context)
    

def add(request):
    if request.method == "POST":
        if "big" not in request.POST:
            big = None
        else:
            big = request.POST['big']
        #create new word 
        new_word = {
            "word": request.POST['word'],
            "color": request.POST['color'],
            "big": big,
            "created_at": datetime.now().strftime("%H:%M %p, %B %d, %Y")
        }
        #append new word
        words = request.session['words']
        words.append(new_word)
        request.session['words'] = words
        print new_word
        return redirect("/")
    else:
        return redirect("/")

def clear(request):
    del request.session["words"]
    return redirect("/")