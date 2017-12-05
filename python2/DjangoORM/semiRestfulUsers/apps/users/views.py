from django.shortcuts import render, redirect
from models import *
# Create your views here.
def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'users/index.html', context)
def new(request):
    return render(request, 'users/new.html')
def edit(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'users/edit.html', context)
def show(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'users/show.html', context)
def create(request):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if len(errors):
            for error in errors:
                messages.error(request, error)
        else:
            User.objects.create(first_name=request.POST['first_name'],
                                last_name=request.POST['last_name'],
                                email=request.POST['email'])
            return redirect("/users")
    else:
        return redirect("/users/new/create")
def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')
def update(request, id):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if len(errors):
            for error in errors:
                messages.error(request, error)
        else:
            user = User.objects.get(id=id)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
    return redirect('/users/'+id)