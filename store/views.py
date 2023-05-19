
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Medicinedetails
from django.contrib.auth.decorators import login_required


# Create your views here.


# def hello(request):
#     return HttpResponse("Hello world")

def home(request):
    return render(request,'index.html')

def registration (request):
    if request.method == 'POST':
        first_name = request.POST['fname'] 
        last_name = request.POST['lname'] 
        username = request.POST['username'] 
        email = request.POST['email'] 
        pass1 = request.POST['pass1'] 
        pass2 = request.POST['pass2'] 
        
        
        if pass1 == pass2 :
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username is already taken")
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email already exists")   
            else:
                user = User.objects.create_superuser(username = username,
                                                     first_name = first_name,
                                                     last_name = last_name,
                                                     email = email,
                                                     password = pass1 )
              
                user.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,"password is not matched...........")
            return redirect('register')               
        
        
    
    return render(request, './signup/registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user =auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("listmedicine")
        else:
            messages.info(request,'invalid user')
            return render(request,'login/login.html')
     
    else:
        return render(request, 'login/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def addmedicine(request):
    if request.method == 'POST':
        name = request.POST['medicinename']
        cmp = request.POST['companyname']
        date = request.POST['date']
        amount =request.POST['amount']
        medicine_details = Medicinedetails(medicine_name = name, company_name=cmp, date=date, amount=amount)
        medicine_details.save()
        return redirect('listmedicine')
    else:    
        return render(request, 'Medicines/create.html')
    
@login_required    
def listmedicine(request):
    medicine = Medicinedetails.objects.all()
    return render(request, 'Medicines/List.html',{'medicine':medicine})


@login_required
def views(request,id):
    medicine = Medicinedetails.objects.get(id=id)
    return render(request,'Medicines/views.html', {'medicine':medicine})   

@login_required   
def delete(request, id):
    med = Medicinedetails.objects.get(id=id)
    med.delete()
    return redirect('listmedicine')

@login_required   
def edit(request,id):
    if request.method == 'POST':
        name = request.POST['medicinename']
        cmp = request.POST['companyname']
        date = request.POST['date']
        amount =request.POST['amount']
        medicine_details = Medicinedetails(medicine_name = name, company_name=cmp, date=date, amount=amount)
        medicine_details.save()
        return redirect('listmedicine')
    
    else:
        upd = Medicinedetails.objects.get(id=id)
        return render(request,'medicines/edit.html', {'upd':upd})

