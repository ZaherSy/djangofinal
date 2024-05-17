from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
	path('', getLogin, name='homepage'),
	path('login', getLogin, name='getLogin'),
	path('doLogin', doLogin, name='doLogin'),
	path('doLogout', doLogout, name='doLogout'),
	# path('Signup',  getSignup, name=' getSignup'),
	# path('doSignup', doSignup, name='doSignup'),
	path('getProducts', getProducts, name='getProducts'),
	# path('updateCard', updateCard, name='updateCard'),
	# path('cart', getCart, name='getCart'),
	# path('checkout', checkOut, name='checkOut'),
	# path('orders', getOrders, name='getOrders'),

]
