from django.shortcuts import render

def registrationPage(request):
    return render(request, "userRegistration/register.html")