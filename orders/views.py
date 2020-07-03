from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from accounts.forms import UserAddressForm
from accounts.models import UserAddress
from cart.models import Cart
from .models import Order
from .utils import id_generator, generate_client_token

client_token = generate_client_token()

try:
    stripe_pub = settings.STRIPE_PUBLISHABLE_KEY
except Exception as e:
    print(e)
    raise NotImplementedError(str(e))


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
    
    try:
        address_added = request.GET.get('address_added')

    except:
        address_added = None
    
    if address_added is None:
        address_form = UserAddressForm()
    else:
        address_form = None
    
    current_addresses = UserAddress.objects.filter(user=request.user)
    billing_addresses = UserAddress.objects.get_billing_addresses(user=request.user)

    if request.method == 'POST':
        print(request.POST)


    if new_order.status == "Finished":
        # cart.delete()
        del request.session['cart_id']
        # del request.session['item_total']

    context = {
        "address_form": address_form,
        "current_addresses": current_addresses,
        "billing_addresses": billing_addresses,
        "client_token": client_token,
        }
    template = "orders/checkout.html"
    return render(request, template, context)
