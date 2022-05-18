from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Страница приложения Lesson_1')


def index11(request):
    return HttpResponse('Страница приложения Lesson_11')


def index1_1(request):
    return HttpResponse('''<p>Hello World!</p>
                        <p>Django is one of the best framework on Python</p>
                        <hr>''')


def index_hello_world(request):
    return HttpResponse('<body><marquee behavior="alternate">'
                        ' Hello World! </marquee></body>')
