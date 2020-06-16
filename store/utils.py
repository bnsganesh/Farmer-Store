import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print(cart)
    items = []
    order = {'get_cart_items':0, 'get_cart_total':0}
    cartItems = order['get_cart_items']
        
    for i in cart:
        try:
            cartItems += cart[i]["quantity"]
                
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]["quantity"])
                
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]
                
            item = {
                'product':{
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                    'slot': product.slot,
                    'stock': product.stock,
                    'desc': product.desc,
                    'netwt': product.netwt
                },
                'quantity': cart[i]["quantity"],
                'get_total': total,
            }
            items.append(item)
        except:
            pass
      
    return {'cartItems':cartItems,'order':order,'items':items}
    
def cartData(request):
    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']
    order = cookieData['order']
    items = cookieData['items']
    return {'cartItems':cartItems,'order':order,'items':items}
    
def guestOrder(request, data):   
    name = data['form']['name']
    phno = data['form']['phno']
       
    cookieData = cookieCart(request)
    items = cookieData['items']
       
    custemor, created = Custemor.objects.get_or_create(
        phno = phno,
    )
    custemor.name = name
    custemor.save()
        
    order = Order.objects.create(
        custemor = custemor,
        complete = False,
    )
        
    for item in items:
        product = Product.objects.get(id=item['product']['id'])
            
        orderItem = OrderItem.objects.create(
            product = product,
            order = order,
            quantity = item['quantity']
        )
    return custemor, order