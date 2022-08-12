from django.urls import path
from unicodedata import name
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('variety/<str:id>/<slug:slug>', views.variety, name='variety'),
    path('rooms', views.rooms, name='rooms'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('update_profile', views.update_profile, name='update_profile'),   
    path('update_password', views.update_password, name='update_password'),   
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('logoutt', views.logoutt, name='logoutt'),
    path('detail/<str:id>/<slug:slug>',views.detail,name='detail'),
    path('dateofstay/<str:id>/<slug:slug>', views.dateofstay, name='dateofstay'),
    path('addtocart', views.addtocart, name='addtocart'),
    path('cartpage', views.cartpage, name='cartpage'),
    path('remove_item', views.remove_item, name='remove_item'),
    path('checkout', views.checkout, name='checkout'),
    path('placeorder', views.placeorder, name='placeorder'), 
    path('paidorder', views.paidorder, name='paidorder'),
    
    
    #MEAL URLS
    path('meals', views.meals, name='meals'),
    path('meal/<str:id>/<slug:slug>', views.meal, name='meal'),
    path('mealcart', views.mealcart, name='mealcart'),
    path('foodcart', views.foodcart, name='foodcart'),
    path('mealcheckout', views.mealcheckout, name='mealcheckout'),
        
    
    #All Subpages
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('basketballcourt',views.basketballcourt,name='basketballcourt'),
    path('crossroadrestuarant',views.crossroadrestuarant,name='crossroadrestuarant'),
    path('grandballroom',views.grandballroom,name='grandballroom'),
    path('gym',views.gym,name='gym'),
    path('meetingroom',views.meetingroom,name='meetingroom'),
    path('reservation',views.reservation,name='reservation'),
    path('skyrestuarant',views.skyrestuarant,name='skyrestuarant'),
    path('swimmingpool',views.swimmingpool,name='swimmingpool'),
]