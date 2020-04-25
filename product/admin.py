from django.contrib import admin

from .models import Product, Size, Colour

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Colour)
admin.site.register(Size)
