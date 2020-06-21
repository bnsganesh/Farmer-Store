from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from . import report
from . import tray_setting
from . import refill
from . import coin_dispenser

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
    
    path('report/', report.report,name="report"),
    path('download_report/', report.download_report,name="download_report"),
    path('email_report/', report.email_report,name="email_report"),
    
    path('add_item/', views.add_item,name="add_item"),
    
    path('tray_setting/', tray_setting.tray_setting,name="tray_setting"),
    path('tray_delete/', tray_setting.tray_delete,name="tray_delete"),
    
    path('refill/', refill.refill,name="refill"),
    path('clear/', refill.clear,name="clear"),
    
    path('coin_dispenser/',coin_dispenser.coin_dispenser, name="coin_dispenser"),
    path('coinRemover/',coin_dispenser.coinRemover, name="coinRemover"),
    
    path('adds/',views.adds,name="adds"),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)