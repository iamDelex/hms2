from django.contrib import admin
from . models import *
# Register your models here.


class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','slug', 'image', 'price','max_order', 'max_order','display', 'created')
    list_display_links = ('id', 'title','slug')
    prepopulated_fields = {'slug':('title',)}
    

class ShippingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','meal', 'shipping_no', 'paid_cart', 'first_name', 'last_name', 'address', 'phone', 'state', 'status', 'admin_remark']
    list_display_link = ['id','user']
    readonly_fields = ['id', 'user', 'meal', 'shipping_no', 'paid_cart', 'first_name', 'last_name', 'address', 'phone', 'state', 'status', 'admin_remark']


class PaidOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total', 'cart_no', 'payment_code', 'paid_item', 'first_name', 'last_name', 'address', 'email', 'location', 'postal_code']
    list_display_link = ['user', 'total', 'cart_no', 'payment_code']
    readonly_fields = ['id', 'user', 'total', 'cart_no', 'payment_code', 'paid_item', 'first_name', 'last_name', 'address', 'email', 'location', 'postal_code']


class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'meal', 'quantity','how_spicey', 'order_no', 'item_paid']
    list_display_link = ['user', 'meal', 'quantity']
    readonly_fields = ['id', 'user', 'meal', 'quantity', 'order_no', 'item_paid']



admin.site.register(Shipping,ShippingAdmin)
admin.site.register(PaidOrder,PaidOrderAdmin)
admin.site.register(Shopcart,ShopcartAdmin)   
admin.site.register(Meal,MealAdmin)  