from django.shortcuts import render

from .models import Product

def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {"product": product}
        template = "product.html"
        return render(request, template, context)
    except:
        raise Http404

