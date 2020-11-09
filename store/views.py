from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from .models.product import Product
from .models.category import Category

def index(request):
    products = Product.get_all_products();
    categories = Category.get_all_categories()
    categoryID = (request.GET.get('category'))
    if categoryID:
        products =Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request,'index.html', data)