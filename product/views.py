from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404

from carts.models import Cart
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = "product/list.html"

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView,  self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug = slug, active = True)
        except Product.DoesNotExist:
            raise Http404("Não encontrado!")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug = slug, active = True)
            instance =  qs.first()
        return instance