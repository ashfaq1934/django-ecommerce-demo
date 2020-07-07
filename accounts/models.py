from django.db import models
from django.conf import settings


class UserDefaultAddress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120, null=True, blank=True)
    county = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

    def get_address(self):
        return "%s, %s, %s, %s" %(self.address, self.city, self.country, self.postal_code)
