from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name="index"),
    path('store/', views.store,name="store"),
    path('cart/', views.cart,name="cart"),
    path('checkout/', views.checkout,name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    
    path('signin/', views.signin,name="signin"),
    path('signout/', views.signout,name="signout"),
    path('home/', views.home,name="home"),
    path('report/', views.report,name="report"),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)