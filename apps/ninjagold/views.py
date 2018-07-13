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
        y={
            "output" : "Earned "+str(x)+" golds from the farm! ("+str(datetime)+")",
            "color" : "green"
        }
    elif request.POST['building'] == "cave":
        x=random.randrange(5,11)
        y={
            "output" : "Earned "+str(x)+" golds from the cave! ("+str(datetime)+")",
            "color" : "green"
        }
    elif request.POST['building'] == "house":
        x=random.randrange(2,6)
        y={
            "output" : "Earned "+str(x)+" golds from the house! ("+str(datetime)+")",
            "color" : "green"
        }
    elif request.POST['building'] == "casino":
        x=random.randrange(-50,51)
        if x>0:
            y={
                "output" : "Entered a casino and won "+str(x)+" golds!!! Woohoo!!! ("+str(datetime)+")",
                "color" : "green"
            }
        elif x == 0:
            y={
                "output" : "Entered a casino and broke even. Eh. ("+str(datetime)+")",
                "color" : "black"
            }
        else:
            y={
                "output" : "Entered a casino and lost "+str(int(math.fabs(x)))+" golds... Ouch... ("+str(datetime)+")",
                "color" : "red"
            }
    request.session['ninja_gold'] += x
    request.session['activities'].insert(0,y)
    print(request.session['activities'])
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')