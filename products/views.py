from django.shortcuts import render

# Create your views here. контроллер, вьюхи
from products.models import ProductCategory, Product
def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)