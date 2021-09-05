from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
import json


def index(request):
    products = Product.objects.all()
    return render(request, 'index_bestellung.html', {'products': products})


def einkaufskorb(request):
    try:
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']

        product = Product.objects.get(id=productId)

        if action == 'plus':
            product.piece = (product.piece + 1)
        elif action == 'minus':
            if product.piece != 0:
                product.piece = (product.piece - 1)

        if product.piece > 0:
            product.in_cart = True
        else:
            product.in_cart = False

        product.save()

        return JsonResponse('data', safe=False)

    except json.decoder.JSONDecodeError:

        cart_itm = Product.objects.filter(in_cart=True)
        return render(request, 'update_item.html', {'cart_itm': cart_itm})
