from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
import random
import math

def index(request):
    if 'ninja_gold' not in request.session:
        request.session['ninja_gold']=0
    if 'activities' not in request.session:
        request.session['activities']=[]
    if 'values' not in request.session:
        request.session['values']=[]
    return render(request, 'ninjagold/index.html')

def process(request):
    datetime=strftime("%Y/%m/%d %#I:%M %p", localtime())
    if request.POST['building'] == "farm":
        x= random.randrange(10,21)
        request.session['ninja_gold'] += x
        request.session['values'].insert(0,int(x))
        y="Earned "+str(x)+" golds from the farm! ("+str(datetime)+")"
        request.session['activities'].insert(0,y)
    elif request.POST['building'] == "cave":
        x=random.randrange(5,11)
        request.session['ninja_gold'] += x
        request.session['values'].insert(0,int(x))
        y="Earned "+str(x)+" golds from the cave! ("+str(datetime)+")"
        request.session['activities'].insert(0,y)
    elif request.POST['building'] == "house":
        x=random.randrange(2,6)
        request.session['ninja_gold'] += x
        request.session['values'].insert(0,int(x))
        y="Earned "+str(x)+" golds from the house! ("+str(datetime)+")"
        request.session['activities'].insert(0,y)
    elif request.POST['building'] == "casino":
        x=random.randrange(-50,51)
        request.session['ninja_gold'] += x
        request.session['values'].insert(0,int(x))
        if x>=0:
            y="Earned "+str(x)+" golds from the casino! ("+str(datetime)+")"
            request.session['activities'].insert(0,y)
        else:
            y="Entered a casino and lost "+str(int(math.fabs(x)))+" golds... Ouch... ("+str(datetime)+")"
            request.session['activities'].insert(0,y)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')