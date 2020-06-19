from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def tray_setting(request):
    if request.method == 'POST':
        slot = int(request.POST.get('slot'))
        try:
            product = Product.objects.get(slot=slot)
            product.name = request.POST.get('name')
            product.stock = int(request.POST.get('stock'))
            product.save()
        except:
            messages.info(request, 'Go to Add_item to Add!')
            pass
    products = Product.objects.all().order_by('slot')
    return render(request,'controls/tray_setting.html', {'products':products,'range':range(1,25)})
    
@login_required(login_url='signin')
def tray_delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        slot = data['slot']
        products = Product.objects.all().filter(slot=slot)
        products.delete()
        print(products)
    return JsonResponse('Tray Cleared', safe=False)