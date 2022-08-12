from email import message
from email.policy import default
from enum import unique
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from pkg_resources import require

# Create your models here.


class Variety(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        db_table = 'variety'
        managed = True
        verbose_name = 'Variety'
        verbose_name_plural = 'Varieties' 
 

class Room(models.Model):
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False)
    room_detail = models.TextField()
    image1 = models.ImageField(upload_to='room', default= 'traveltourhotel.jpg')
    image2 = models.ImageField(upload_to='room', default= 'traveltourhotel.jpg')
    image3 = models.ImageField(upload_to='room', default= 'traveltourhotel.jpg')
    bed = models.CharField(max_length=10)
    price = models.IntegerField()
    discount = models.FloatField()
    # adult = models.IntegerField(default=1)
    # children = models.IntegerField(default=1)
    signature = models.BooleanField()
    suites = models.BooleanField()
    garden = models.BooleanField()
    display = models.BooleanField(default=False)
    available = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        db_table = 'room'
        managed = True
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'



       
STATUS = [
    ('New', 'New'),
    ('Pending', 'Pending'),
    ('Processing', 'Processing'),
    ('Closed', 'Closed'),
]
      
class Contact(models.Model):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    closed = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='New')
    
    def __str__(self):
        return str(self.first_name)
    
    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True )
    email = models.EmailField(blank=True,null=True)
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    class Meta:
        db_table = 'profile'
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    


class Booking(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    order_no = models.CharField(max_length=36)
    item_paid = models.BooleanField(default=False)
    no_day  = models.IntegerField(blank=True, null=True)    
    
    def __str__(self):
        return f'{self.user.username}'


class PaidBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    cart_no = models.CharField(max_length=36, blank=True, null=True)
    payment_code = models.CharField(max_length=36)
    paid_item = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    
    
    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        db_table = 'paidBooking'
        managed = True
        verbose_name = 'PaidBooking'
        verbose_name_plural = 'PaidBooking'
        
class Bannerword(models.Model):
    text = models.CharField(max_length=300, blank=True) 
    slogan = models.CharField(max_length=300, blank=True)
    
    
    def __str__(self):
        return str(self.text)
 