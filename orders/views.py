from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from accounts.models import UserDefaultAddress
from cart.models import Cart
from .models import Order, OrderDetails
from .forms import OrderDetailsForm
from .utils import id_generator, generate_client_token, transact


def orders(request):
    context = {}
    template = "orders/user.html"
    return render(request, template, context)

@login_required
def order_details(request):
    print(request.POST)
    try:
        # get the session for a user's cart
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except Cart.DoesNotExist:
        the_id = None
        return HttpResponseRedirect(reverse('cart'))
    
    try:
        # get the session for a user's cart
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except Cart.DoesNotExist:
        the_id = None
        return HttpResponseRedirect(reverse('cart'))
    
    try:
        default_address = UserDefaultAddress.objects.get(user=request.user)
        initial = {
                'address': default_address.address,
                'city': default_address.city,
                'county': default_address.county,
                'postal_code': default_address.postal_code,
                'phone_number': default_address.phone_number

            }
        form = OrderDetailsForm(request.POST or None, initial=initial)
    except UserDefaultAddress.DoesNotExist:
        form = OrderDetailsForm(request.POST or None)
    
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
        new_order_details = OrderDetails.objects.get(order=new_order)
        form = None

    except OrderDetails.DoesNotExist:
        if form.is_valid():
            new_order_details = form.save(commit=False)
            new_order_details.order = new_order
            new_order_details.address = form.cleaned_data.get("address")
            new_order_details.city = form.cleaned_data.get('city')
            new_order_details.country = form.cleaned_data.get('county')
            new_order_details.postal_code = form.cleaned_data.get('postal_code')
            new_order_details.phone_number = form.cleaned_data.get('phone_number')
            new_order_details.save()

            is_default = form.cleaned_data.get("default")
            if is_default:
                try:
                    default_address = UserDefaultAddress.objects.get(user=request.user)
                    default_address.address = form.cleaned_data.get("address")
                    default_address.city = form.cleaned_data.get('city')
                    default_address.county = form.cleaned_data.get('county')
                    default_address.postal_code = form.cleaned_data.get('postal_code')
                    default_address.phone_number = form.cleaned_data.get('phone_number')
                    default_address.save()
                except UserDefaultAddress.DoesNotExist:
                    default_address = UserDefaultAddress()
                    default_address.user = request.user
                    default_address.address = form.cleaned_data.get("address")
                    default_address.city = form.cleaned_data.get('city')
                    default_address.county = form.cleaned_data.get('county')
                    default_address.postal_code = form.cleaned_data.get('postal_code')
                    default_address.phone_number = form.cleaned_data.get('phone_number')
                    default_address.save()  
    except:
        return HttpResponseRedirect(reverse('cart'))

    template = 'orders/order_details.html'
    context = {
        'form': form,
        }

    return render(request, template, context)


@login_required
def checkout(request, **kwargs):
    client_token = generate_client_token()
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
        new_order = None
        return HttpResponseRedirect(reverse('cart'))

    result = transact({
            'amount': new_order.final_total,
            'payment_method_nonce': request.POST.get('payment_method_nonce', None),
            'options': {
                "submit_for_settlement": True
            }
        })

    if result.is_success or result.transaction:
        print('it worked')


    if new_order.status == "Finished":
        # cart.delete()
        del request.session['cart_id']
        del request.session['item_total']

    context = {
        "client_token": client_token,
        }
    template = "orders/checkout.html"
    return render(request, template, context)
