from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.forms import forms
from .models import Product
from .form import ProductForm

# Create your views here


# TODO
"""
    product_create_view,
    product_detail_view,
    product_list_view
"""


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }

    return render(request, 'products/create.html', context)


def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj
    }
    return render(request, "products/detail.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/product_list.html", context)
