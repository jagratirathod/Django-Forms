from django.shortcuts import render
from .forms import Signupform,Loginform

from django.http import HttpResponse
# from django.core.files.storage import FileSystemStorage
from . import models
from datetime import date
from django.contrib.auth import authenticate




def signup(request):
    # form=Signupform()
    if request.method=="POST":
        form=Signupform(request.POST, request.FILES)
        
        if form.is_valid(): 
            # file = request.FILES['file']
            # fs = FileSystemStorage()
            # filename = fs.save(file.name, file)

            #image = request.FILES['image']
            #fs = FileSystemStorage()
            # filename = fs.save(image.name, image)
            print("form.cleaned_data['image']", form.cleaned_data['image'])
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            mobile=form.cleaned_data['mobile']
            married=form.cleaned_data['married']
            unmarried=form.cleaned_data['unmarried']
            gender=form.cleaned_data['gender']
            game=form.cleaned_data['game']
            file=form.cleaned_data['file']
            image=form.cleaned_data['image']
            z=models.Register(email=email,password=password,first_name=firstname,last_name=lastname,mobile=mobile,married=married,unmarried=unmarried,gender=gender,game=game,file=file,image=image,date=datetime.today())
            z.save()
            return HttpResponse("Successfully Signup")
            
    else:
        form=Signupform()
        return render(request,"signup.html",{"form":form})

    
def login(request):
    if request.method=="POST":
        form=Loginform(request.POST)
        print(form.is_valid())
        
        if form.is_valid():
            user=models.Register.objects.filter(email=form.cleaned_data['email'],password=form.cleaned_data['password']).first()
            print(user)
            if user:
                return render(request,"login.html",{"output":"Succcessfully login","form":form})
            else:
                return render(request,"login.html",{'output':'Invalid User',"form":form})
    
    form=Loginform()
    return render(request,"login.html",{"form":form})

        
