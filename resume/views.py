import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Resume


def create_resume(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'resume/create.html')
        elif request.method == "POST":
            data = json.loads(request.body)
            data["author"] = request.user.profile
            Resume.objects.create(**data)
            return JsonResponse({"message": "Резюме успешно создано"}, status=201)
    else:
        return redirect("root:login")


def all_resumes(request):
    if request.method == "GET":
        resumes = Resume.objects.all()
        return render(request, 'resume/list.html', context={"resumes": resumes})


def get_by_id(request, id):
    if request.method == "GET":
        resume = Resume.objects.filter(id=id).first()
        if resume:
            return render(request, 'resume/view.html', context={"resume": resume})
        else:
            return render(request, 'root/404.html')
    elif request.method == "POST":
        resume = Resume.objects.filter(id=id).first()
        if resume:
            if request.user.is_authenticated:
                if resume.author.user == request.user:
                    data = json.loads(request.body)

                    for field, value in data.items():
                        setattr(resume, field, value)

                    resume.save()
                    return JsonResponse({"message": "Резюме обновлено"}, status=200)
                else:
                    return JsonResponse({"message": "Нет доступа"}, status=403)
            else:
                return JsonResponse({"message": "Отсутствует авторизация"}, status=401)
        else:
            return render(request, 'root/404.html')


def get_by_username(request, username):
    if request.method == "GET":
        user = User.objects.filter(username=username).first()
        if user:
            return render(request, 'resume/list.html', context={"resumes": user.profile.resumes.all()})
        else:
            return render(request, 'root/404.html')
