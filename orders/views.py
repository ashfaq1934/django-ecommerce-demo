from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order
from .utils import id_generator


def orders(request):
    context = {}
    template = "orders/user.html"
    return render(request, template, context)

@login_required
def checkout(request):
    try:
        # get the session for a user's cart
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except Cart.DoesNotExist:
        the_id = None
        return HttpResponseRedirect(reverse('cart'))
    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        return HttpResponseRedirect(reverse('cart'))

    if new_order.status == "Finished":
        # cart.delete()
        del request.session['cart_id']
        # del request.session['item_total']

    context = {}
    template = "home.html"
    return render(request, template, context)
