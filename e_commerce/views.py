from django.shortcuts import render
from django.views.generic import ListView
from product.views import Product


class ProductListViewHomePage(ListView):
    model = Product
    template_name = "home_page.html"
    paginate_by = 3 