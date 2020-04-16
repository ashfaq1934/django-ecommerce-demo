from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120, default='product_%s' %{id})
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, default=title)

    def __str__(self):
        return self.title
    
    def get_price(self):
        return self.price

