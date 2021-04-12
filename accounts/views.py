# views.py

from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect
from .forms import RegisterForm

from django.contrib.auth.hashers import (

    Clear, MD5PasswordHasher, UnsaltedMD5PasswordHasher, AesMD5
)


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid() == True:

            user = form.save()
            case = response.POST['password_management']
        
            if case == '1':
                user.password = make_password(response.POST['password2'],None,'clear')
                user.save(update_fields=['password'])
                print("CHECK PASSWORD")
                if check_password(response.POST['password2'],user.password):
                    print("OUI")
                else:
                    print("NON")
            elif case == '2':
                user.password = make_password(response.POST['password2'],None,'unsalted_md5')
                user.save(update_fields=['password'])
            elif case == '3':
                user.password = make_password(response.POST['password2'],None,'md5')
                user.save(update_fields=['password'])
            elif case == '4':
                user.password = "md5$"+response.POST['salt']+"$"+response.POST['password2']
                user.save(update_fields=['password'])
            elif case == '5':
                user.password = make_password(response.POST['password2'],response.POST['salt'],'aesMD5')
                user.save(update_fields=['password'])
            else:
                print("CASE DEFAULT => ERROR")



            print(response.POST)
            
            return redirect("/admin")
    else:
        form = RegisterForm()
        return render(response, "registration/signup.html", {"form":form})