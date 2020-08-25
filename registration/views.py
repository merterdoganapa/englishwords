from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def registerUser(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        if username and email and password == confirm:
            newUser = User(username=username,email=email)
            newUser.set_password(password)
            newUser.save()
            return redirect("login")
        else:
            context = {
                'error' : "Parolar Eşleşmiyor",
            }
            render(request,"register.html",context=context)
    return render(request,"register.html")
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")

    return render(request,"login.html")
def logoutUser(request):
    logout(request)
    messages.warning(request,'Çıkış Yaptınız')
    return redirect("index")