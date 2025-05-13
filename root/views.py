from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


from django.contrib.auth.models import User

from resume.models import Profile


def index(request):
    return render(request, 'root/main.html')


def contacts(request):
    return render(request, 'root/contacts.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'root/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        user = User.objects.filter(username=username).first() or User.objects.filter(email=email).first()
        if user:
            return JsonResponse({"message": "username или email уже заняты"}, status=400)
        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user)
        login(request, user)
        return JsonResponse({"message": "ok"}, status=200)


def login_view(request):
    if request.method == 'GET':
        return render(request, 'root/login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # убедись, что поле называется именно так

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"message": "ok"}, status=200)
        else:
            return JsonResponse({"message": "Неверный логин или пароль"}, status=400)

def logout_view(request):
    logout(request)
    return redirect('root:main')