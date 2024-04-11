from django.shortcuts import render

# Create your views here.
def Register(request):
    return render(request, 'Register.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')