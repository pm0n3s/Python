from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
    return render(request, 'loginreg/index.html')

def create(request):
    if request.method == "POST":
        errors = User.objects.regval(request.POST)
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('/')
        else:
            safepw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=safepw)
            request.session['first_name'] = request.POST['first_name']
            return render(request, 'loginreg/success.html')
    else:
        return redirect('/')

def show(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if user:
            password = user[0].password
            if bcrypt.checkpw(request.POST['password'].encode(), password.encode()):
                request.session['first_name'] = user[0].first_name
                return render(request, 'loginreg/success.html')
            else:
                return redirect('/')
        else:
            messages.error(request, 'email not found')
            return redirect('/')  