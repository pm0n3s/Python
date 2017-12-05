from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'index.html')


def process_money(request):
    if request.method == "POST":
        building = request.POST['building']
        if 'activity' not in request.session:
            request.session['activity'] = []
        activity = request.session['activity']

        if building == 'casino':
            gold = random.randint(-50, 50)
            if gold < 0:
                activity.append("Entered a " + building + " and lost " + str(gold) + " gold...Ouch..")
            else:
                activity.append("Entered a " + building + " and won " + str(gold) + " gold!")
        else:
            if building == 'farm':
                gold = random.randint(10, 20)      
            elif building == 'cave':
                gold = random.randint(5, 10)           
            elif building == 'house':
                gold = random.randint(2, 5) 
            activity.append("Earned " + str(gold) + " gold from " + building + "!")           

        request.session['gold'] = int(request.session['gold']) + gold
        request.session['activity'] = activity
        return redirect('/')
