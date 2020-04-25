from django.db import models
from product.models import Product, Size, Colour

class CartItem(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Size, null=True, blank=True)
    colours = models.ManyToManyField(Colour, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    notes = models.CharField(null=True, blank=True, max_length=300)
    line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        try:            
            return str(self.cart.id)
        except:
            return self.product.title

class Cart(models.Model):
    products = models.ManyToManyField(Product, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Cart id: %s" %(self.id)