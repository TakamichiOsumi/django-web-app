from django.shortcuts import render
from . import views

# Create your views here.
def products(request):
    return render(request, 'products/products.html')
