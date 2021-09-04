from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
import json


def index(request):
    products = Product.objects.all()
    return render(request, 'index_bestellung.html', {'products': products})


def updateItem(request):
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

        product.save()

    except json.decoder.JSONDecodeError:
        print("String could not be converted to JSON")

    return JsonResponse('data', safe=False)
