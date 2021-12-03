from django.shortcuts import render

def index(request):
    return HttpResponse(‘Главная страница‘)

def group_posts(request):
    return HttpResponse(f’блог‘{pk}’)