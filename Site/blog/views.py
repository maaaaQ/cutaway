from django.shortcuts import render
from .models import News

# Create your views here.


def home(request):
    data = {
        "title": "Главная страница",
        "news": News.objects.all(),
    }
    return render(request, "blog/home.html", data)


def about(request):
    data = {
        "title": "Подробнее обо мне:",
        "name": "Макеев Юрий",
        "age": 29,
        "edu": 'Рузаевский Политехнический Техникум по специальности "Автоматизированные системы обработки информации и управления"',
        "main_skills": "Опыт работы с:  Python - ООП, HTML, CSS, Bootstrap, Django, PostgreSQL, GitHub",
        "plans": "Django REST Framework",
    }
    return render(request, "blog/about.html", data)
