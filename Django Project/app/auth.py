from django.shortcuts import render, redirect
from django.contrib import auth

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == "GET":
        return render(request, "auth/login.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # username and password are correct 
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                next = ""
                if "next" in request.GET:
                    next = request.GET["next"]
                if next == None or next == "":
                    next = "/"
                return redirect(next)
            else:
                return render(request, "auth/login.html", {"warning" : "Your account is disabled" })

        else:
            return render(request, "auth/login.html", {"warning" :"Inavlid username and password"})

def register(request):
    if request.method == "GET":

        return render(request,"auth/register.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        auth.models.User.objects.create_user(username, email, password).save()
        user = auth.authenticate(username = username, password=password)
        auth.login(request,user)
        return render(request, "auth/registered.html")

