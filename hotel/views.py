import json
from multiprocessing import context
import uuid
import requests



from typing import Any
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView,FormView
from hotel.booking_functions.availability import check_availability

from hotel.models import *
from hotel.forms import *
from food.forms import *
from food.models import *

# Create your views here.

def index(request):
    varieties = Variety.objects.all()
    bannercontent = Bannerword.objects.all()
    
    context = {
        'varieties':varieties,  
        'bannercontent':bannercontent,
    }
    return render(request, 'index.html', context)

def rooms(request):
    rooms = Room.objects.all()
    #.filter(available=True)
    
    context={
        'rooms':rooms,
    }     
    return render(request, 'rooms.html', context)



#USER PROFILE 
@login_required(login_url='signin')
def user_profile(request):
    user_profile = Profile.objects.get(user__username=request.user.username)
    context = {
        'user_profile':user_profile
    }
    return render(request, 'user_profile.html',context)

#USER UPDATE PROFILE 
@login_required(login_url='signin')
def update_profile(request):
    update_profile = Profile.objects.get(user__username=request.user.username)
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            data=form.save()
            messages.success(request, f'{data.user} your profile is updated successful🙂')
            return redirect('user_profile')
    
    context = {
        'update_profile':update_profile,
        'form':form,
    }
    return render(request, 'update_profile.html',context)

#changepassword
@login_required(login_url='signin')
def update_password(request):
    load_profile = Profile.objects.get(user__username=request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, f'Your password has been updated successfully ✅✅✅')
            return redirect('user_profile')
        else:
            messages.error(request, form.errors)
            return redirect('password-update')
               
    
    context = {
        'load_profile':load_profile,
        'form':form
    }
    return render(request, 'update_password.html', context)
#changepassword done

#contact 
def contact(request):
    cform = ContactForm() #instantiate an empty form for a GET request
    if request.method == 'POST':
        cform = ContactForm(request.POST)#instantiate the form for a POST request
        if cform.is_valid():
            cform.save()
            messages.success(request, 'Thank you for contacting us, Our Customer Care will reach you soon😊')
            return redirect('index')
        else:
            messages.error(request, cform.errors)
            return redirect('index')
    
    context = {
        'cform':cform
    }
    
    return render(request,'index.html', context)
#contact done


#register 
def register(request):   
    form = RegisterForm() #instantiate the reistration form for a GET request
    if request.method =='POST': # check if a POST method for persisting data to the DB
        email = request.POST['email']
        form = RegisterForm(request.POST) # instantiate the reisterform for a POST request
        if form.is_valid(): # ensures security checks here
            user = form.save() # save data if data is valid
            profile = Profile(user = user)
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            profile.email = email
            profile.save()
            login(request, user)
            messages.success(request, f'{user.username} Your Registeration Was Successful😊')
            return redirect('index') # send user any page you desire, in this case Homepage
        else:
            messages.error(request, form.errors)
            return redirect('register')
    
    context = {
        'form':form
    }    
    return render(request, 'register.html', context)
#register done

#signin 
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request, user)
            messages.success(request, f'welcome {user.username}, You have successfully login!')
            return redirect('index')
        else:
            messages.error(request, f'Wrong Username or Password!, Please Enter A Correct Username And Password.')
            return redirect('signin')
    
    context = {    }
    
    return render(request, 'signin.html', context)
#signin done

def logoutt(request):
    logout(request)
    messages.success(request, f'You Have Successfully Logout')
    return redirect('signin')

# //////////////////////////////////   SUBPAGES VIEW PAGES   ///////////////////////////////////
#about 
def about(request):       
    return render(request, 'about.html')
#about done

#basketballcourt 
def basketballcourt(request):       
    return render(request, 'basketballcourt.html')
#basketballcourt

#cart 


# Addtocart;
@login_required(login_url='signin')
def addtocart(request):
    cartno = Profile.objects.get(user__username=request.user.username)
    cart_code = cartno.id
    if request.method == 'POST':
        checkin = request.POST['arrival_date']
        checkout = request.POST['depature_date']
        addid = request.POST['dateid']
        cartid = Room.objects.get(pk=addid)
        
        
        # instantiate the cart for prospective user
        cart = Booking.objects.filter(user__username=request.user.username,item_paid=False)
        
        if cart:  # instantiate the cart for a selected item
            more = Booking.objects.filter(room_id=cartid.id,check_in = checkin, check_out =checkout, user__username=request.user.username)
            if more:
                more.user = request.user
                more.check_in = checkin
                more.check_out = checkout
                if more.check_in > checkout or more.check_out < checkin:
                    more.save()
                    messages.success(request, 'Room booked successfull')
                    return redirect('rooms')    
                else:
                    messages.info(request, 'The room you requested is not available for the dates stated, Please enter a new date.')
                    return redirect('index')
                
            else: #add new items to cart
                newitem = Booking()
                newitem.user = request.user
                newitem.room = cartid
                newitem.check_in = checkin
                newitem.check_out = checkout
                newitem.order_no = cart_code
                newitem.item_paid = False
                newitem.save()
                messages.success(request, 'added!')
                return redirect('rooms')
                
        else: # create a cart
            newcart = Booking()
            newcart.user = request.user
            newcart.room = cartid
            newcart.check_in = checkin
            newcart.check_out = checkout
            newcart.order_no = cart_code
            newcart.item_paid = False
            newcart.save()
            messages.success(request, f'This room has been added to your cart, kindly checkout or continue')
            
    return redirect('rooms')
# Addtocart Done

# cart 
@login_required(login_url='signin')
def cartpage(request):
    # Booking.objects.filter(item_paid=True).delete()
    cart = Booking.objects.filter(user__username=request.user.username,item_paid=False)
    
    for item in cart:
        item.no_day = (item.check_out - item.check_in).days 
        item.save()
    
    total = 0
    vat = 0
    subtotal = 0
    
    for item in cart:
        if item.room.discount:
            subtotal += item.room.discount * item.no_day
        else:
            subtotal += item.room.price * item.no_day
                        
    vat = 0.075 * subtotal # please note that, vat is at 7.5% of the subtotal, that is 75/100 * subtotal
    total = vat + subtotal   # Please note, Addition of vat and subtotal gives the total value to be charged
    
    context = {
        'cart':cart,
        'subtotal':subtotal,
        'vat':vat,
        'total':total,    
        }
       
    return render(request, 'cartpage.html', context)
# cart done


@login_required(login_url='signin')
def remove_item(request): #This is the function to remove an item from the cart page.
    deleteitem = request.POST['deleteitem']
    Booking.objects.filter(pk=deleteitem).delete()
    messages.success(request, 'Room successfully deleted from your cart')
    return redirect('cartpage')


#checkout 
@login_required(login_url='signin')
def checkout(request):       
    cart = Booking.objects.filter(user__username=request.user.username,item_paid=False)
    user_profile = Profile.objects.get(user__username=request.user.username)
    
    for item in cart:
        item.no_day = (item.check_out - item.check_in).days 
        item.save()
    
    total = 0
    vat = 0
    subtotal = 0
    
    for item in cart:
        if item.room.discount:
            subtotal += item.room.discount * item.no_day
        else:
            subtotal += item.room.price * item.no_day
                        
    vat = 0.075 * subtotal # please note that, vat is at 7.5% of the subtotal, that is 75/100 * subtotal
    total = vat + subtotal   # Please note, Addition of vat and subtotal gives the total value to be charged
    
    context = {
        'cart':cart,
        'subtotal':subtotal,
        'vat':vat,
        'total':total,  
        'user_profile':user_profile,  
        }
       
    return render(request, 'checkout.html', context)
#checkout

#placeorder
@login_required(login_url='signin')
def placeorder(request):
    if request.method == 'POST':
        #collect data to send to paystack.
        # the api_key(registration programming interface key) and curl will be sourced from paystack site, 
        # paystack will give text secret key for testing, when you want to go liv, paystack will give live key.
        # cburl (callback url),total,ref_num,order_num,email provided by me in my application, 
        api_key = 'sk_test_728b856f01a2849f148286c26ca2dcdc61870fbd' #This is from paystack
        # api_key = 'sk_test_1690919ca38995c567f6aa2748e35877709b5ff4' #This is from paystack
        curl = 'https://api.paystack.co/transaction/initialize' #This is from paystack Api documentation
        cburl = 'http://18.130.184.224/paidorder' #This ip '18.130.184.224' address is from the one i got from AWS.
        ref_num = str(uuid.uuid4())
        cartno = Profile.objects.get(user__username=request.user.username)
        # order_num = cartno.id
        total = float(request.POST['get_total']) * 100
        phone = request.POST['phone']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = User.objects.get(username = request.user.username)
        
        
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'reference':ref_num, 'amount':int(total), 'callback_url':cburl, 'email':user.email, 'currency':'NGN'}
        print('TESTING DATA LOAD', data)
        #collect data to send to paystack done.
        
        #call to paystack
        try:
            r = requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, 'Network busy, please refresh and try again. Thank You.')   
        else:
            transback = json.loads(r.text)
            rd_url = transback['data']['authorization_url']  
            # take record of transactions made done
            
            # take record of transactions made
            paid = PaidBooking()
            paid.user = user
            paid.total = total/100
            # paid.cart_no = order_num
            paid.payment_code = ref_num
            paid.paid_item = True
            paid.first_name = first_name
            paid.last_name = last_name
            paid.email = user.email
            paid.phone = phone
            paid.save()
            
            #we are trying to empty our cart page after payment as been done.
            booked = Booking.objects.filter(user__username = request.user.username, item_paid=False)
            for item in booked:
                item.item_paid = True
                item.save()
                
                done = Room.objects.get(pk = item.room.id)
                done.available = False
                done.save()
            return redirect(rd_url)
        return redirect('checkout')  
        #call to paystack done, when transaction is successful is redirected to the callback page.



#Thank you page
def paidorder(request):
    profile = Profile.objects.get(user__username = request.user.username)
        
    context = {
        'profile':profile,
    }
    
    return render(request, 'paidorder.html', context)
#Thank you page done



#crossroadrestuarant 
def crossroadrestuarant(request):       
    return render(request, 'crossroadrestuarant.html')
#crossroadrestuarant

#signature 
def variety(request, id, slug):
    variety = Room.objects.filter(variety_id=id) 
    single = Variety.objects.get(pk=id)
    context={
        'variety': variety,
        'single':single,
    }
    return render(request, 'variety.html',context)
#signature

#detail 
def detail(request, id,slug):  
    detail = Room.objects.get(pk=id)
    context={
        'detail':detail,
    }     
    return render(request, 'detail.html',context)
#detail

#dateofstay 
def dateofstay(request,id,slug):   
    detail = Room.objects.get(pk=id)
    context={
        'detail':detail,
    } 
    return render(request, 'dateofstay.html',context)
#dateofstay

#paidorder 
def paidorder(request): 
    paid=Profile.objects.get(user__username=request.user.username)
    context = {
        'paid':paid,
    }
    return render(request, 'paidorder.html', context)
#paidorder

#bookingdetail 
def bookingdetail(request):  
    return render(request, 'bookingdetail.html')
#bookingdetail

#grandballroom 
def grandballroom(request):       
    return render(request, 'grandballroom.html')
#grandballroom

#gym 
def gym(request):       
    return render(request, 'gym.html')
#gym

#meetingroom 
def meetingroom(request):       
    return render(request, 'meetingroom.html')
#meetingroom

#reservation 
def reservation(request):
    book = Booking.objects.filter(user__username=request.user.username)
    context = {
        'book':book,
    }   
    return render(request, 'reservation.html', context)
#reservation

#skyrestuarant 
def skyrestuarant(request):       
    return render(request, 'skyrestuarant.html')
#skyrestuarant

#swimmingpool 
def swimmingpool(request):       
    return render(request, 'swimmingpool.html')
#swimmingpool





# //////////////////////////////////   SUBPAGES VIEWS PAGES DONE   ///////////////////////////////////





# food business logic 
from food.models import *

# Create your views here.
def meals(request):
    meals = Meal.objects.all() #This is show casing all the meals we have in our DB.
        
    context = {
        'meals':meals,
    }
    return render(request, 'meals.html', context)

def meal(request, id,slug):
    meal = Meal.objects.get(pk=id) #This is getting each meals by their specify ID. in this place, we use objects.get
    
    context = {
        'meal':meal,    }
    return render(request, 'meal.html', context)

@login_required(login_url='signin')
def mealcart(request):
    cartno = Profile.objects.get(user__username=request.user.username)
    cartno = cartno.id
    if request.method == 'POST':
        addquantity = int(request.POST['quantity'])
        addspice = request.POST['how_spicey']
        addid = request.POST['mealid']
        mealid = Meal.objects.get(pk=addid)
        # addspicy = request.POST.get('spicy', None)
        
        
        # instantiate the cart for prospective user
        cart = Shopcart.objects.filter(user__username=request.user.username,item_paid=False)
        
        if cart:  # instantiate the cart for a selected item
            more = Shopcart.objects.filter(meal_id=mealid.id,user__username=request.user.username).first()
            if more:
                more.quantity += addquantity
                more.how_spicey += addspice
                more.save()
                messages.success(request, 'Product added to shopcart!')
                return redirect('meals')
            else: #add new items to cart
                newitem = Shopcart()
                newitem.user = request.user
                newitem.meal = mealid
                newitem.quantity = addquantity
                newitem.how_spicey = addspice
                newitem.order_no = cartno
                newitem.item_paid = False
                newitem.save()
                messages.success(request, 'added!')
                return redirect('meals')
                
        else: # create a cart
            newcart = Shopcart()
            newcart.user = request.user
            newcart.meal = mealid
            newcart.quantity = addquantity
            newcart.how_spicey = addspice
            newcart.order_no = cartno
            newcart.item_paid = False
            newcart.save()
            messages.success(request, f'Item has been added to your shopcart 🛒')
            
    return redirect('meals')



@login_required(login_url='signin')
def foodcart(request):
    cart =Shopcart.objects.filter(user__username=request.user.username, item_paid=False)
    
    total = 0
    var = 0
    subtotal = 0
    
    for item in cart:
        subtotal += item.meal.price * item.quantity
                        
    var = 0.075 * subtotal # please note that, vat is at 7.5% of the subtotal, that is 75/100 * subtotal
    total = var + subtotal   # Please note, Addition of vat and subtotal gives the total value to be charged
    context = {
        'cart':cart,
        'subtotal':subtotal,
        'var':var,
        'total':total,    }
    return render(request, 'foodcartpage.html',context)



@login_required(login_url='signin')
def remove_item(request): #This is the function to remove an item from the cart page.
    deleteitem = request.POST['deleteitem']
    Shopcart.objects.filter(pk=deleteitem).delete()
    messages.success(request, 'Item successfully deleted from your shopcart')
    return redirect('meals')


@login_required(login_url='signin')
def mealcheckout(request):
    cart = Shopcart.objects.filter(user__username=request.user.username,item_paid=False)
    user_profile = Profile.objects.get(user__username=request.user.username)
    total = 0
    var = 0
    subtotal = 0
    
    for item in cart:
        subtotal += item.meal.price * item.quantity
            
    var = 0.075 * subtotal # please note that, vat is at 7.5% of the subtotal, that is 75/100 * subtotal
    total = var + subtotal   # Please note, Addition of vat and subtotal gives the total value to be charged
    context = {
        'cart':cart,
        'total':total,
        'user_profile':user_profile,
        # 'orderno': cart[0].order_no
    }
    return render(request, 'checkoutfood.html', context)
