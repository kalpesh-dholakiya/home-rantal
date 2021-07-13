from django.shortcuts import render,redirect,HttpResponse
from Home_Rental_System.models import Registration

# Create your views here.
#Added By Priya
def index(request):
    return render(request,'index.html')

def about(request):
   return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def apartment(request):
    return render(request,'apartment.html')

def registrationpage(request):
    if request.method=="POST":
        registration=Registration()
        registration.email_id=request.POST.get('txt_email')
        registration.fname=request.POST.get('txt_fname')
        registration.lname=request.POST.get('txt_lname')
        registration.gender=request.POST.get('re_ga')
        registration.phone_no=request.POST.get('txt_pnumber')
        registration.password=request.POST.get('txt_password')
        registration.user_type=request.POST.get('ddl')

       # registration=Registration(email_id=email_id,fname=fname,lname=lname,gender=gender,phone_no=phone_no,password=password,user_type=user_type)
        registration.save()
        return redirect('/')

    elif request.method=="GET":
         return render(request,'registrationpage.html')

def login(request):
    if request.method=="POST":
        check_auth=Registration.objects.filter(email_id=request.POST.get('txt_email'),password=request.POST.get('txt_password'),user_type=request.POST.get('ddl')).count()
        if check_auth==1:
            request.session['auth']=Registration.objects.get(email_id=request.POST.get('txt_email')) 
            return redirect('/')
        else:
            return render(request,'login.html',{"error":"Invalid username or password !..."})    
    if request.method=="GET":
        data=request.session.get("auth")
        if data!="":
            return redirect('/')
        else:
            return render(request,'login.html')   
def logout(request):
    data=request.session.get("auth")
    if data!="":
        request.session.clear()
        return redirect('/login')
    else:
        return render(request,'login.html')                  
                   



