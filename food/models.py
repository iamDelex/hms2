from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False)
    image = models.ImageField(upload_to='meal', default= 'meal.jpg')
    price = models.IntegerField()
    min_order = models.IntegerField(default=1)
    max_order = models.IntegerField(default=20)
    display = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'meal'
        managed = True
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'
        
    
      
class Shopcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    how_spicey = models.CharField(max_length=50)
    order_no = models.CharField(max_length=50)
    item_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'shopcart'
        managed = True
        verbose_name = 'Shopcart'
        verbose_name_plural = 'Shopcarts'
    
    
    
class PaidOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    cart_no = models.CharField(max_length=36, blank=True, null=True)
    payment_code = models.CharField(max_length=36)
    paid_item = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=70)
    postal_code = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'paidOrder'
        managed = True
        verbose_name = 'PaidOrder'
        verbose_name_plural = 'PaidOrders'


    
STATUS =[
    ('new', 'new'),
    ('ppending', 'ppending'),
    ('processing', 'processing'),
    ('shipping', 'shipping'),
    ('delivered', 'delivered'),
]  
class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, blank=True, null=True)
    shipping_no = models.CharField(max_length=50)
    paid_cart = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='new', blank=True, null=True)
    admin_remark = models.CharField(max_length=100,  blank=True, null=True)
    
    def __str__(self):
        return self.user
    
    class Meta:
        db_table = 'shipping'
        managed = True
        verbose_name = 'Shipping'
        verbose_name_plural = 'Shippings'