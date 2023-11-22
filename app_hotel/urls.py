
from django.contrib import admin
from django.urls import path
from app_hotel import views

urlpatterns = [

    # URL For Login,Signup and Logout
   path('',views.user_login,name="login"),
   path('signup/', views.sign_up,name="signup"),
   path('logout/',views.user_logout,name='logout'),

   # URL For Dashboard,Base and Reservation
   path('dashboard/',views.dashboard,name='dashboard'),
   path('base/',views.base,name='base'),


   # URL For Room 
   path('room/',views.room,name='room'),
   path('addroom/', views.addroom, name='addroom'),
   path('room/delete/<int:id>/',views.deleteroom,name='deleteroom'),
   path('room/update/<int:id>/',views.updateroom,name='updateroom'),
   
   # URL For Staff
   path('staff/',views.staff,name='staff'),
   path('addstaff/', views.addstaff, name='addstaff'),
   path('staff/delete/<int:id>/',views.deletestaff,name='deletestaff'),
   path('staff/update/<int:id>/',views.updatestaff,name='updatestaff'),

   # URL For Customer
   path('customer/',views.customer,name='customer'),
   path('addcustomer/',views.addcustomer,name='addcustomer'),
   path('customer/delete/<int:id>/',views.deletecustomer,name='deletecustomer'),
   path('customer/update/<int:id>/',views.updatecustomer,name='updatecustomer'),

   # URL For Reservation
   path('reservation/',views.reservation,name='reservation'),
   path('addreservation/',views.addreservation,name='addreservation'),
   path('reservation/delete/<int:id>/',views.deletereservation,name='deletereservation'),
   path('reservation/update/<int:id>/',views.updatereservation,name='updatereservation'),

]

