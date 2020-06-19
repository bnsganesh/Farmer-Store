from django.shortcuts import render, redirect
from .models import *

from django.http import JsonResponse
import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def coin_dispenser(request):
    coins = CoinDispenser.objects.all().order_by('date_added')
    context = {}
    try:
        coin = CoinDispenser.objects.latest('date_added')
        total = coin.total
        count = coin.count
        
        if request.method == 'POST':
            try:
                value = int(request.POST.get('value'))
                count = int(request.POST.get('count'))
                total += value * count
                coin = CoinDispenser(value=value, count=count, total=total, added=value)
                coin.save()
                context = {'coins':coins, 'total':10, 'count':5}
            except:
                print("Exception")
                pass
        context = {'coins':coins, 'total':total, 'count':count}
    except:
        context = {'coins':coins}
        pass
    return render(request, 'controls/coin_dispenser.html', context)
    
@login_required(login_url='signin')
def coinRemover(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            coin = CoinDispenser.objects.latest('date_added')
            total = coin.total
            value = data['value']
            count = data['count']
            total -= value * count
            coin = CoinDispenser(value=value, count=count, total=total, deleted=value)
            coin.save()
        except:
            print("Exception")
            pass
    return JsonResponse('Coin Removed', safe=False)