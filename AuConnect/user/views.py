from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.

def login(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, "Giriş başarılı")
            return redirect("index")
        else :
            messages.add_message(request, messages.ERROR, "Kullanıcı adı veya parola yanlış...")
            return redirect("login")
    else:
        return render(request, 'user/login.html')

def register(request):
    if request.method == "POST": 
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        if password == repassword:
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, "Bu kullanıcı adı daha önce alınmış")
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING, "Bu email daha önce alınmış")
                    return redirect('register')
                else:
                    #burası çalışıyosa hiç bir sorun yok kaydetme yapılabilir
                    user = User.objects.create_user(username = username, password = password, email = email)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, "Kullanıcı oluşturuldu")
                    return redirect('login')
        else:
            messages.add_message(request, messages.WARNING, "Parolalarınız eşleşmiyor")
            return redirect("register")
    else:
        return render(request, "user/register.html")
    

def logout(request):

    if request.method == "POST":
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, "Oturum kapatıldı")
        return redirect('index')
    else:
        return render(request, "user/logout.html")


