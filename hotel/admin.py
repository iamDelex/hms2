from django.contrib import admin
from .models import *
# Register your models here.
class VarietyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created', 'updated')
    list_display_links = ('id','name', 'slug')
    prepopulated_fields = {'slug':('name',)}
    
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id','available','variety','name','slug','image1','image2','image3','bed','price','discount','signature','suites','garden','display','created','updated')
    list_display_links = ['id','variety','name','slug']
    list_editable = ['display','discount','bed','price']
    prepopulated_fields = {'slug':('name',)}

class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'room', 'check_in', 'check_out','order_no','no_day','item_paid']
    list_display_links = ['id', 'user', 'room', 'check_in']
    
class PaidBookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'total', 'cart_no', 'paid_item', 'first_name', 'last_name', 'phone', 'email']
    list_display_link = ['user', 'total', 'cart_no']
    readonly_fields = ['user', 'total', 'cart_no', 'paid_item', 'first_name', 'last_name', 'phone', 'email']
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'message', 'created','status', 'closed']
    list_display_links = ['id', 'first_name', 'last_name', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'first_name', 'last_name', 'address', 'state', 'phone', 'email']
    list_display_links = ['user', 'first_name', 'last_name', 'address', 'state', 'phone', 'email']

class BannerwordAdmin(admin.ModelAdmin):
    list_display = ['text', 'slogan']
    list_display_links = ['text', 'slogan']
    

admin.site.register(Variety,VarietyAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(PaidBooking,PaidBookingAdmin)
admin.site.register(Bannerword,BannerwordAdmin)
