from django.contrib import admin

from .models import Order, OrderDetails, Coupon

admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Coupon)
