from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def refill(request):
    if request.method == 'POST':
        slot = int(request.POST.get('slot'))
        try:
            product = Product.objects.get(slot=slot)
            product.stock = int(request.POST.get('stock'))
            product.save()
        except:
            messages.info(request, 'No Product exist!')
            pass
    products = Product.objects.all().order_by('slot')
    return render(request,'controls/refill.html', {'products':products,'range':range(1,25)})
    
@login_required(login_url='signin')
def clear(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        slot = data['slot']
        try:
            product = Product.objects.get(slot=slot)
            product.stock = int(0)
            product.save()
        except:
            print(type(slot))
            pass
    return JsonResponse('Stock Cleared', safe=False)