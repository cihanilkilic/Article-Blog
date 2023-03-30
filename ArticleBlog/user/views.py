from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def User_Register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                context = {
                    "error": "Kullanıcı adı zaten kullanılıyor!",
                    "username": username,
                    "email": email,
                    "firstname": firstname,
                    "lastname": lastname,
                    
                }
                return render(request, "user/register.html",context)
            
            if User.objects.filter(email=email).exists():
                context = {
                    "error": "Mail adresi zaten kullanılıyor!",
                    "username": username,
                    "email": email,
                    "firstname": firstname,
                    "lastname": lastname,
                }
                return render(request, "user/register.html",context)
            else:
                    New_User = User.objects.create_user(
                    username=username, email=email, first_name=firstname, last_name=lastname, password=password)
                    New_User.save()
                    login(request, New_User)
                    # messages.success(request,"tenks")
                    return redirect("home:index")
        else:
            return render(request, "user/register.html", {
                "error": "Parolalar eşleşmiyor!",
                "username": username,
                "email": email,
                "firstname": firstname,
                "lastname": lastname
            })
    return render(request,"user/register.html")




def User_Login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        context = {
        "form":form,
        "error":"Kullanıcı adı veya parola hatalı!",
    }
    if form.is_valid():
        New_User = authenticate(username=username, password=password)
        if New_User is None:
            #messages.info(request,"Kullanıcı adı veya parola hatalı!")
            return render(request,"user/login.html",context)
        else:
            login(request,New_User)
            return redirect("home:index")
    return render(request,"user/login.html")





def logoutView(request):
    logout(request)
    return redirect("user:Login")