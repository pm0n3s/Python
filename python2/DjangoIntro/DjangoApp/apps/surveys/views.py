from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("placeholder to display all the surveys created")

def new(reqest):
    return HttpResponse("placeholder for users to add a new survey")