from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create(request):
    if request.method == "POST":
        print "this is hit"
        Course.objects.create(name=request.POST['name'],
                            desc=request.POST['desc'],)
    return redirect('/')
def destroy(request, id):
    if request.method == "POST":
        Course.objects.get(id=id).delete()
        return redirect('/')
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'courses/destroy.html', context)