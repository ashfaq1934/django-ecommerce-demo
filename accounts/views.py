from django.shortcuts import render, HttpResponseRedirect, Http404, reverse
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegistrationForm
from .models import UserDefaultAddress


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):

    form = LoginForm(request.POST or None)
    btn = 'Login'

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password, backend='django.contrib.auth.backends.ModelBackend')
        login(request, user)

    context = {
        "form": form,
        "btn": btn,
    }
    
    template = "form.html"
    return render(request, template, context)

def registration_view(request):

    form = RegistrationForm(request.POST or None)
    btn = 'Join'

    if form.is_valid():
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password')
        # user = authenticate(username=username, password=password, backend='django.contrib.auth.backends.ModelBackend')
        # login(request, user)
        new_user = form.save(commit=False)
        new_user.first_name = 'Justin'
        new_user.save()

    context = {
        "form": form,
        "btn": btn,
    }
    
    template = "form.html"
    return render(request, template, context)

# def add_user_address(request):
#     try:
#         next_page = request.GET.get("next")
#     except:
#         next_page = None

#     if request.method == "POST":
#         form = UserAddressForm(request.POST)
#         if form.is_valid():
#             new_address = form.save(commit=False)
#             new_address.user = request.user
#             new_address.save()
#             is_default = form.cleaned_data.get("default")
#             if is_default:
#                 default_address, created = UserDefaultAddress.objects.get_or_create(user=request.user)
#                 default_address.shipping = new_address
#                 default_address.save()
#             if next_page is not None:
#                 return HttpResponseRedirect(reverse(str(next_page))+'?address_added=True')
#     else:
#         return Http404
