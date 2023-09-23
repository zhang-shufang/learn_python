from django.shortcuts import render

# Create your views here.
def index(request):
    """披萨店主页"""
    return render(request, 'pizzaria_apps/index.html')