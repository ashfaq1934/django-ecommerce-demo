from django.contrib import admin
from django.urls import path, re_path
from cart.views import view, update_cart
from product.views import single

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^cart/$', view, name='cart'),
    re_path(r'^cart/(?P<slug>[\w-]+)//(?P<qty>\d+)/$', update_cart, name='update_cart'),
    re_path(r'^products/(?P<slug>[\w-]+)/$', single, name='single_product')
]