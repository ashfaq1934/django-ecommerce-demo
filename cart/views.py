from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
import json
from .models import Cart, CartItem
from product.models import Product

def view(request):
    try:
        #create a session for a user's cart
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        #if the session was created and the id was defined and the cart items retrieved, display them
        cart = Cart.objects.get(id=the_id)
        context = {"cart": cart}
    else:
        #otherwise display emoty message
        empty_message = 'Your cart is empty'
        context = {"empty": True, 
                    "empty_message": empty_message}

    template = 'cart/view.html'
    return render(request, template, context)

def update_cart(request, slug):
    #set expiry time if user doesn't log out
    request.session.set_expiry(120000)
    try:
        #get product quantity from the form
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False
    
    note = {}
    
    try:
        colour = request.GET.get('colour')
        #add colour to notes dictionary
        note['colour'] = colour
    except:
        colour = None
    
    try:
        size = request.GET.get('size')
        #add size to notes dictionary
        note['size'] = size
    except:
        size = None
    
    print(colour)
    print(size)
    print(note)

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
    #create the cart item based on the session's cart id and the product chosen
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if update_qty and qty:

        if int(qty) <= 0:
            #if the quantity is 0 or less, delete the cart item
            cart_item.delete()
        else:
            #otherwise, set the quantity and save the item
            cart_item.quantity = qty
            cart_item.notes = json.dumps(note)
            cart_item.save()
    else:
        pass
    
    new_total = 0.00
    for item in cart.cartitem_set.all():
        line_total = float(item.product.price) * item.quantity
        new_total += line_total
    
    request.session['items_total'] = cart.cartitem_set.count()
    #set the cart's total as the new total by gettingthe count
    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse("cart"))