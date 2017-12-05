from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "first_app/index.html", context)
def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = request.POST['name']
        print "*"*50
        return redirect("/")