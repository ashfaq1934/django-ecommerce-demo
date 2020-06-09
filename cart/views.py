from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
import json
from .models import Cart, CartItem
from product.models import Product, Variation

def view(request):
    try:
        # get the session for a user's cart
        the_id = request.session['cart_id']
        # if the session was created and the id was defined and the cart items retrieved, display them
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
    if the_id:
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
            
        request.session['items_total'] = cart.cartitem_set.count()
        # set the cart's total as the new total by gettingthe count
        cart.total = new_total
        cart.save()
        # success message
        context = {"cart": cart}
    else:
        #otherwise display empty message
        empty_message = 'Your cart is empty'
        context = {"empty": True, 
                    "empty_message": empty_message}

    template = 'cart/view.html'
    return render(request, template, context)

def remove_from_cart(request, id):
    try:
        #get the session for a user's cart
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("cart"))
    
    cartitem = CartItem.objects.get(id=id)
    cartitem.delete()
    # cartitem.cart = None
    # cartitem.save()
    # send success message
    return HttpResponseRedirect(reverse("cart"))


def add_to_cart(request, slug):
    #set expiry time if user doesn't log out
    request.session.set_expiry(120000)

    try:
        #update the sessions cart, othetwise create a new cart
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass

    except:
        pass

    product_variations = []
    
    if request.method == 'POST':
        qty = request.POST['qty']
        for item in request.POST:
            key = item
            value = request.POST[key]
            try:
                variation = Variation.objects.get(product=product, category__iexact=key, title__iexact=value)
                product_variations.append(variation)
            except:
                pass

        #create the cart item based on the session's cart id and the product chosen
        cart_item = CartItem.objects.create(cart=cart, product=product)
        #otherwise, set the quantity and save the item
        if len(product_variations) > 0:
                cart_item.variations.add(*product_variations)
        cart_item.quantity = qty
        cart_item.save()
        return HttpResponseRedirect(reverse("cart"))
    return HttpResponseRedirect(reverse("cart"))