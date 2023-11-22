from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse 
from app_hotel.models import Room,Staff,Customer,Reservation
from .forms import RoomForm,StaffForm,CustomerForm,ReservationForm

# Create your views here.

# VIEW FOR SIGNUP
def sign_up(request):

    if request.method == "POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully')
            fm.save()

            login_url = reverse('login')  # redirect to login page after successfully signing up
            return HttpResponseRedirect(login_url)
    else:
        fm=SignUpForm()

    return render(request,'app_hotel/signup.html',{'form':fm})


# VIEW FOR LOGIN
def user_login(request):
    # if not request.user.is_authenticated:
        if request.method == "POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                #  used to store and retrieve cleaned (validated) data that a user has submitted
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']

                # verify the user's credentials ... returns object if the credentials are correct or None if not correct
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    
                    login(request,user)
                    # print("User Successfully Logged In")
                    messages.success(request, 'Login successful')
                    
                    # Use reverse to generate the URL for the 'base' view
                    return HttpResponseRedirect(reverse('base'))
                
                else:
                     messages.error(request, 'Username or password is incorrect. Please try again.')

        else:
            fm=AuthenticationForm()
        return render(request,'app_hotel/login.html',{'form':fm})


# VIEW FOR LOGOUT
def user_logout(request):
    logout(request)
    login_url=reverse('login')
    return HttpResponseRedirect(login_url)


# VIEW FOR DASHBOARD
def dashboard(request):
    return render(request,'app_hotel/dashboard.html')


# VIEW FOR BASE
def base(request):
    return render(request,'app_hotel/base.html')


# VIEW FOR ROOM
def addroom(request):
    room = Room.objects.all()
    return render(request,'app_hotel/addroom.html',context={'room':room})

def room(request):
    if request.method == 'POST':
        rm = RoomForm(request.POST)

        if rm.is_valid():
            rnumber = rm.cleaned_data['room_number']
            rtype = rm.cleaned_data['room_type']
            rprice = rm.cleaned_data['room_price']
            rdescription = rm.cleaned_data['description']
            ravailable = rm.cleaned_data['is_available']

            reg = Room(room_number=rnumber,room_type=rtype,room_price=rprice,description=rdescription,is_available=ravailable)
            reg.save()

            return redirect('addroom')
    else:
        rm = RoomForm()
    room = Room.objects.all()
    return render(request,'app_hotel/room.html',{'rm':rm,'room':room})

# TO UPDATE ROOM
def updateroom(request,id):
    if request.method=="POST":
        rm=Room.objects.get(pk=id)
        fm = RoomForm(request.POST,instance=rm)

        if fm.is_valid():
            fm.save()
    else:
        rm=Room.objects.get(pk=id)
        fm = RoomForm(instance=rm)
    return render(request,'app_hotel/updateroom.html',{'form':fm})

# TO DELETE ROOM
def deleteroom(request,id):
    if request.method == "POST":
        room = Room.objects.get(pk=id)
        room.delete()
        return HttpResponseRedirect(reverse('addroom'))


# VIEW FOR STAFF
def addstaff(request):
    staff = Staff.objects.all()
    return render(request,'app_hotel/addstaff.html',context={'staff':staff})

def staff(request):
    if request.method == 'POST':
        st = StaffForm(request.POST)

        if st.is_valid():
            fname = st.cleaned_data['first_name']
            lname = st.cleaned_data['last_name']
            email = st.cleaned_data['email']
            phone = st.cleaned_data['phone_number']
            position = st.cleaned_data['position']

            reg = Staff(first_name=fname,last_name=lname,email=email,phone_number=phone,position=position)
            reg.save()

            return redirect('addstaff')
    else:
        st = StaffForm()
    staff = Staff.objects.all()
    return render(request,'app_hotel/staff.html',{'st':st,'staff':staff})

# TO UPDATE STAFF
def updatestaff(request,id):
    if request.method=="POST":
        st=Staff.objects.get(pk=id)
        fm = StaffForm(request.POST,instance=st)

        if fm.is_valid():
            fm.save()
    else:
        st=Staff.objects.get(pk=id)
        fm = StaffForm(instance=st)
    return render(request,'app_hotel/updatestaff.html',{'form':fm})

# TO DELETE STAFF
def deletestaff(request,id):
    if request.method == "POST":
        
        staff = Staff.objects.get(pk=id)
        staff.delete()

        return HttpResponseRedirect(reverse('addstaff'))
    

# VIEW FOR CUSTOMER

def addcustomer(request):
    customers = Customer.objects.all()
    return render(request,'app_hotel/addcustomer.html',{'customer':customers})

def customer(request):
    if request.method == 'POST':
        ct = CustomerForm(request.POST)

        if ct.is_valid():
            fname = ct.cleaned_data['first_name']
            lname = ct.cleaned_data['last_name']
            email = ct.cleaned_data['email']
            phone = ct.cleaned_data['phone_number']

            reg = Customer(first_name=fname,last_name=lname,email=email,phone_number=phone)
            reg.save()
            
            return redirect('addcustomer')
    else:
        ct = CustomerForm()
    customer = Customer.objects.all()
    return render(request,'app_hotel/customer.html',{'ct':ct,'customer':customer})

# TO UPDATE CUSTOMER
def updatecustomer(request,id):
    if request.method=="POST":
        ct=Customer.objects.get(pk=id)
        fm = CustomerForm(request.POST,instance=ct)
        if fm.is_valid():
            fm.save()
    else:
        ct=Customer.objects.get(pk=id)
        fm = CustomerForm(instance=ct)
    return render(request,'app_hotel/updatecustomer.html',{'form':fm})

# TO DELETE CUSTOMER
def deletecustomer(request,id):
    if request.method == "POST":
        customer = Customer.objects.get(pk=id)
        customer.delete()
        return HttpResponseRedirect(reverse('addcustomer'))
    

# VIEW FOR RESERVATION
def addreservation(request):
    reservation = Reservation.objects.all()
    return render(request,'app_hotel/addreservation.html',{'reservation':reservation})

def reservation(request):
    if request.method == 'POST':
        rs = ReservationForm(request.POST)

        if rs.is_valid():
            cname = rs.cleaned_data['customer_name']
            checkin = rs.cleaned_data['check_in_date']
            checkout = rs.cleaned_data['check_out_date']
            room = rs.cleaned_data['room']
            ispaid = rs.cleaned_data['is_paid']
            total = rs.cleaned_data['total_amount']
            createdby = rs.cleaned_data['created_by']

            reg = Reservation(customer_name=cname,check_in_date=checkin,check_out_date=checkout,room=room,is_paid=ispaid,total_amount=total,created_by=createdby)
            reg.save()
            
            return redirect('addreservation')
    else:
        rs = ReservationForm()
    reservation = Reservation.objects.all()
    return render(request,'app_hotel/reservation.html',{'rs':rs,'reservation':reservation})

# TO UPDATE RESERVATION
def updatereservation(request,id):
    if request.method=="POST":
        rs=Reservation.objects.get(pk=id)
        fm = ReservationForm(request.POST,instance=rs)
        if fm.is_valid():
            fm.save()
    else:
        rs=Reservation.objects.get(pk=id)
        fm = ReservationForm(instance=rs)
    return render(request,'app_hotel/updatereservation.html',{'form':fm})

# TO DELETE RESERVATION
def deletereservation(request,id):
    if request.method == "POST":
        reservation = Reservation.objects.get(pk=id)
        reservation.delete()
        return HttpResponseRedirect(reverse('addreservation'))
    


