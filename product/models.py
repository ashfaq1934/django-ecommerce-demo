from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120, default='product_%s' %{id})
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, default=title)
    stock_levels = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_price(self):
        return self.price


class VariationManager(models.Manager):

    def all(self):
        return super(VariationManager, self).filter(active=True)

    def sizes(self):
        return self.all().filter(category='size')
    
    def colours(self):
        return self.all().filter(category='colour')


VAR_CATEGORIES = (
    ('size', 'size'),
    ('colour', 'colour'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=100, choices=VAR_CATEGORIES, default='size')
    price = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    objects = VariationManager()

    def __str__(self):
        return self.title
