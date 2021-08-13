from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Category, Product
from cart.forms import CartAddProductForm

cart_product_form = CartAddProductForm()

def catalog(request):
    categorys = Category.objects.order_by()
    return render(request, 'catalog/catalog.html', {'categorys' : categorys})

def category_detail(requset, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.order_by()
    context = {'products' : products, 'category' : category, 'cart_product_form': cart_product_form}
    return render(requset, 'catalog/category_detail.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product' : product, 'cart_product_form': cart_product_form}
    return render(request, 'catalog/product_detail.html', context)







