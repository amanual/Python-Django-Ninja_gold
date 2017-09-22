from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

# Create your views here.
def index(request):
    
    if 'count' not in request.session:
        request.session['count'] = 0  
    if 'num' not in request.session:
        request.session['num'] = []
    print request.session['num']    
    return render(request, 'ninja_gold/index.html')

def process_money(request):  
    time = strftime('%Y-%m-%d %H:%S', gmtime()) 
    if request.POST['building'] == 'farm':
        gold = random.randrange(10, 21)
        time = strftime('%Y-%m-%d %H:%S', gmtime()) 
        print time        
        request.session['num'].append("Earned: {} golds from the farm! {}".format(gold,time))
       
    elif request.POST['building'] == 'cave':
        gold = random.randrange(5, 10)        
        request.session['num'].append("Earned: {} golds from the cave! {}".format(gold, time))
        
    elif request.POST['building'] == 'house':
        gold = random.randrange(2, 5)
        request.session['num'].append("Earned: {} golds from the house! {}".format(gold, time))
        
    elif request.POST['building'] == 'casino':
        gold = random.randrange(-50, 50)
        if gold < 0:
            request.session['num'].append("Entered a casino and lost {} golds...Ouch..! {}".format(gold, time))
        else:
            request.session['num'].append("Earned: {} golds from the casino! {}".format(gold, time))
    
    request.session['count'] += gold  
    return redirect('/')    

def reset(request):         
    request.session['count'] = 0
    request.session['num'] = []
    return redirect('/')
