from django.shortcuts import render

# Create your views here.
def register__view(request):
    return render(request, 'register.html')
def login__view(request):
    return render(request, 'login.html')
def logout__view(request):
    pass
