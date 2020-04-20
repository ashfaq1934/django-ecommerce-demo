from django.contrib import admin

from .models import Product, Variation

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
