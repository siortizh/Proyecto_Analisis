# calculator/views.py

from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def metodos(request):
    return render(request, 'metodos.html')
