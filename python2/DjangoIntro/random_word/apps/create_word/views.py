from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    if "counter" not in request.session:
        request.session["counter"] = 0
    else:
        request.session["counter"] += 1
    content = {
        "word": get_random_string(length=14),
    }
    return render(request,'create_word/index.html', content)

def generate(request):
    return redirect("/")

def reset(request):
    try:
        del request.session["counter"]
    except:
        pass
    return redirect("/")