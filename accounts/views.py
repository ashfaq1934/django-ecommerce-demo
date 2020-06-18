from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegistrationForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):

    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password, backend='django.contrib.auth.backends.ModelBackend')
        login(request, user)

    context = {
        "form": form,
    }
    
    template = "form.html"
    return render(request, template, context)

def registration_view(request):

    form = RegistrationForm(request.POST or None)

    # if form.is_valid():
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password')
        # user = authenticate(username=username, password=password, backend='django.contrib.auth.backends.ModelBackend')
        # login(request, user)

    context = {
        "form": form,
    }
    
    template = "form.html"
    return render(request, template, context)
