from django.shortcuts import render

def index(request):
    return render(request, 'petstagram/index.html')