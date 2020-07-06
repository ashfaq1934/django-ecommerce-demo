from django.contrib import admin
from .models import UserStripe, UserDefaultAddress

# Register your models here.

admin.site.register(UserStripe)
admin.site.register(UserDefaultAddress)