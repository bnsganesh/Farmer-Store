from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utils import cartData, cookieCart, guestOrder

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ProductForm

def index(request):
        return render(request,'index.html')
        
def store(request):
    data = cartData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    products=Product.objects.all().order_by('stock')
    context={'products':products, 'cartItems':cartItems}
    return render(request,'store/store.html',context)

def cart(request):
    data = cartData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    context={'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'store/cart.html',context)
    
def checkout(request):
    data = cartData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    context={'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'store/checkout.html',context)    
    
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']   
    custemor = request.user.custemor
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(custemor=custemor, complete=False)   
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()        
    return JsonResponse('Item was added', safe=False)
    
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    custemor, order = guestOrder(request, data)
    
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == float(order.get_cart_total):
        order.complete = True
    order.save()            
    return JsonResponse('Payment submitted', safe=False)
    
def signin(request):
    if(request.user.is_authenticated):
        return redirect('home')
    else:
        if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is In-Correct !')
        
    context = {}
    return render(request,'controls/signin.html', context)

def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def home(request):
    return render(request,'controls/home.html')
       
@login_required(login_url='signin')       
def add_item(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if(form.is_valid):
            print("Valid")
        else:
            print("In-Valid")
    else:
        print("GET")
        form = ProductForm()
    return render(request,'controls/add_item.html', {'form':form})