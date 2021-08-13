from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from catalog.models import Category
from cart.cart import Cart
from cart.forms import CartAddProductForm
import uuid
from yookassa import Configuration, Payment

Configuration.account_id = "827165"
Configuration.secret_key = "test_dwxIiqOGKRKOweO7fffyTllqWOEKqnBdPUN-V6NoAcs"

def pay(request):
    cart = Cart(request)
    summ = cart.get_total_price()
    payment = Payment.create({
        "amount": {
            "value": str(summ),
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "http://127.0.0.1:8000/"
        },
        "capture": True,
        "description": "Заказ №1"
    })
    return HttpResponseRedirect(payment.confirmation.confirmation_url)

def home(request):
    categorys = Category.objects.order_by()
    return render(request, 'main/home.html', {'categorys' : categorys})

def partners(request):
    categorys = Category.objects.order_by()
    return render(request, 'main/partners.html', {'categorys' : categorys})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')


