
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Room,Staff,Customer,Reservation


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']


# Room Form
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets={
            'room_number':forms.TextInput(attrs={'class':'form-control'}),
            'room_type':forms.TextInput(attrs={'class':'form-control'}),
            'room_price':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'is_available':forms.CheckboxInput(attrs={'class':'form-control'})
        }


# Staff Form
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'})
        }

# Customer Form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
        }


# Reservation Form
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets={
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'check_in_date': forms.DateInput(attrs={'class': 'form-control'}),
            'check_out_date': forms.DateInput(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
            'is_paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),}