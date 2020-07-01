from django.contrib import admin
from django.urls import path, re_path
from cart.views import view, add_to_cart, remove_from_cart
from product.views import single
from accounts.views import logout_view, login_view, registration_view, add_user_address
from orders.views import checkout, orders


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^cart/$', view, name='cart'),
    re_path(r'^cart/(?P<id>\d+)/$', remove_from_cart, name='remove_from_cart'),
    re_path(r'^cart/(?P<slug>[\w-]+)/$', add_to_cart, name='add_to_cart'),
    re_path(r'^products/(?P<slug>[\w-]+)/$', single, name='single_product'),
    re_path(r'^checkout/$', checkout, name='checkout'),
    re_path(r'^orders/$', orders, name='user_orders'),
    re_path(r'^accounts/logout/$', logout_view, name='auth_logout'),
    re_path(r'^accounts/login/$', login_view, name='auth_login'),
    re_path(r'^accounts/register/$', registration_view, name='auth_registration'),
    re_path(r'^add_user_address/$', add_user_address, name='add_user_address'),
]
