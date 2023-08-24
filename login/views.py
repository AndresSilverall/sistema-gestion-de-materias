from django.shortcuts import render

# Create your views here.
def form_login(request):
    return render(request, "login.html")