from django.shortcuts import render
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
from .models import product_content


def layout(request):
    return render(request, 'Myapp/layout.html')
def cart(request):
    return render(request, 'Myapp/cart.html')
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
