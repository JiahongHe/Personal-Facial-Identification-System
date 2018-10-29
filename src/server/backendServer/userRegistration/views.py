from django.shortcuts import render
from django.http import HttpResponse
from .forms import registrationForm

def registrationPage(request):

    # serves the user registration page

    if request.method == 'GET':
        form = registrationForm()
        context = {"form": form}
        return render(request, "userRegistration/register.html", context)

def register(request):

    # handles the submitted user registration form, validate it and save it to the database.

    if request.method == 'POST':
        form = registrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("you are ready to go!")
        else:
            return HttpResponse("invalid form, please go back and send it again")

    return render(request, "userRegistration/register.html")