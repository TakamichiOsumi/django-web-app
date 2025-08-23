from django.shortcuts import render
from django.views import generic
from .models import Product

# Create your views here.
class Products(generic.TemplateView):
    model = Product
    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.products = Product.objects.all()
        context['products'] = self.products
        return context

products = Products.as_view()
