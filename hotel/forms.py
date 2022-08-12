from dataclasses import fields
import profile
from random import choice
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from hotel.models import *



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
        
STATE=[
    ('Abia','Abia'), 
    ('Adamawa','Adamawa'),
    ('Akwa Ibom','Akwa Ibom'),
    ('Anambra','Anambra'), 
    ('Bauchi','Bauchi'),
    ('Bayelsa','Bayelsa'), 
    ('Benue','Benue'),
    ('Borno','Borno'),
    ('Cross River','Cross River'),
    ('Delta','Delta'),
    ('Ebonyi','Ebonyi'),
    ('Edo','Edo'),
    ('Ekiti','Ekiti'), 
    ('Enugu','Enugu'), 
    ('Gombe','Gombe'), 
    ('Imo','Imo'), 
    ('Jigawa','Jigawa'),
    ('Kaduna','Kaduna'),
    ('Kano','Kano'),
    ('Katsina','Katsina'),
    ('Kebbi','Kebbi'),
    ('Kogi','Kogi'),
    ('Kwara','Kwara'),
    ('Lagos','Lagos'), 
    ('Nasarawa','Nasarawa'), 
    ('Niger','Niger'), 
    ('Ogun','Ogun'),
    ('Ondo','Ondo'),
    ('Osun','Osun'),
    ('Oyo','Oyo'), 
    ('Plateau','Plateau'),
    ('Rivers','Rivers'),
    ('Sokoto','Sokoto'),
    ('Taraba','Taraba'),
    ('Yobe','Yobe'),
    ('Zamfara','Zamfara'),
]
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {'first_name', 'last_name', 'address', 'state', 'phone','email'}
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'state':forms.Select(attrs={'class':'form-control', 'placeholder':'State'}, choices=STATE),
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}),
        }
        
class RegisterForm(UserCreationForm):
    email = forms.EmailInput()
        
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class BookingForm(forms.ModelForm):
    arrival_date = forms.DateField(required=True)
    depature_date = forms.DateField(required=True)
    
    class Meta:
        model = Booking
        fields = ['arrival_date','depature_date']