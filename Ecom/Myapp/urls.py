from django.urls import path 
from . import views 


urlpatterns = [
    path('products', views.product, name='products'),
    path('cart', views.cart, name='cart'),
    path('signin', views.signin, name='signin'),
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('login', views.login, name='login'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('increment/<int:product_id>/', views.increment, name='increment'),
    path('decrement/<int:product_id>/', views.decrement, name='decrement'),
]

