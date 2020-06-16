from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)

    context = {
        "form": form,
    }
    
    template = "form.html"
    return render(request, template, context)
