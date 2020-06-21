from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse, HttpResponse
import json

from django.contrib.auth.decorators import login_required

from .forms import OrderForm
from .filters import OrderFilter

import csv
from django.core.mail import EmailMessage

@login_required(login_url='signin')       
def report(request):

    orders=Order.objects.all().order_by('-date_ordered')
    
    myFilter = OrderFilter(request.POST, queryset=orders)
    orders = myFilter.qs
    
    global csvfile
    csvfile = HttpResponse(content_type='text/csv')
    csvfile['Content-Disposition'] = 'attachment;filename="report.csv"'
    writer = csv.writer(csvfile)
    writer.writerow(['Date','Transaction ID','Custemor','Items','Amount'])
    
    for order in orders:
        writer.writerow([order.date_ordered,order.transaction_id,order.custemor.name,order.items,order.amount])
    
    global context
    context={'orders':orders, 'myFilter':myFilter}
    
    return render(request,'controls/report.html', context)

@login_required(login_url='signin')
def download_report(request):
    return csvfile

@login_required(login_url='signin')
def email_report(request):
    global csvfile
    email = EmailMessage(
        'Report - storeff',
        'Farmers Fridge',
        'storefarmersfridge@gmail.com',
        [request.user.email],
    )
    email.attach('csvfile.csv', csvfile.getvalue(), 'text/csv')
    email.send()
    global context
    return JsonResponse('Email Sent!', safe=False)