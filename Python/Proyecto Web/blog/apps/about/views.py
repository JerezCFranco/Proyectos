from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about/about.html')

def probar(request):
    return render(request, 'probar/probar.html')

