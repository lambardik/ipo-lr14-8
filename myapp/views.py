from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def tema(request):
    return render(request, 'tema.html')

def me(request):
    return render(request, 'me.html')
