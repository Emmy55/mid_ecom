from django.shortcuts import render, redirect
from django.http import JsonResponse
# from django.shortcuts import get_object_or_404

# from shopping_cart.models import Order

# from .models import Profile


# def my_profile(request):
#     my_user_profile = Profile.objects.filter(user=request.user).first()
#     my_orders = Order.objects.filters(is_ordered=True, owner=my_user_profile)
#     context = {
#         'my_orders' : my_orders
#     }
#     return render(request, 'profile.html', context)

# # Create your views here.

from .models import content
from .models import product_content, Cart


def add_to_cart(request, product_id):
    product = content.objects.get(id=product_id)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart.objects.create(user=request.user, product=product)
    return redirect('cart')

def increment(request, product_id):
    product = content.objects.get(id=product_id)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    data = {
        'success': True,
        'message': 'Product added to cart successfully'
    }
    return JsonResponse(data)

def decrement(request, product_id):
    product = content.objects.get(id=product_id)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()
    if cart_item.quantity <= 1:
        cart_item.delete()
        return redirect('cart')
    if cart_item:
        cart_item.quantity -= 1
        cart_item.save()
    data = {
        'success': True,
        'message': 'Products decucted sucessfully'
    }
    return JsonResponse(data)

def layout(request):
    return render(request, 'Myapp/layout.html')
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum([item.product.price * item.quantity for item in cart_items])
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'Myapp/cart.html', context)
def signin(request):
    return render(request, 'Myapp/signin.html')
def login(request):
    return render(request, 'Myapp/login.html')
def forgot_password(request):
    return render(request, 'Myapp/forgot.html')


def home(request):
    home_products = content.objects.all()
    return render(request, 'Myapp/home.html', {
        'all' : home_products
    })


def product(request):
    products = product_content.objects.all()
    return render(request, 'Myapp/product.html', {
        'view' : products
    })
