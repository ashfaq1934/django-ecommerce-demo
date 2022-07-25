from django.contrib.auth import get_user_model
from django.db import models

from cart.models import Cart

User = get_user_model()

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    coupon_used = models.BooleanField(default=False)
    final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    order_id = models.CharField(max_length=120, default="ABC", unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id

class OrderDetails(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=120, null=True)
    city = models.CharField(max_length=120, null=True)
    county = models.CharField(max_length=120, null=True)
    postal_code = models.CharField(max_length=120, null=True)
    phone_number = models.CharField(max_length=120, null=True)

    def __str__(self):
        return str(self.order)

class Coupon(models.Model):
    code = models.CharField(max_length=20)
    discount_percentage = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    num_available = models.IntegerField(default=1)
    num_used = models.IntegerField(default=0)

    def __str__(self):
        return self.code
