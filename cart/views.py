from django.shortcuts import render, HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    # return redirect('catalog:product_detail')
    # len_cart = print(len(cart))
    # print(len_cart)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    url = request.META.get('HTTP_REFERER', '/')
    url += '#openModal'
    return redirect(url)


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    print('Жопа')
    return render(request, 'PATH/TEMPLATE.html', {'cart': cart})
