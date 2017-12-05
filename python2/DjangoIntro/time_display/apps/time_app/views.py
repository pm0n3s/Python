from django.shortcuts import render
from time import gmtime, strftime, localtime
# Create your views here.
def index(request):
    context = {
        'time1': strftime("%b %d, %Y", gmtime()),
        'time2': strftime("%H:%M %p", gmtime())
    }
    return render(request,"time_app/index.html", context)