from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

# Create your views here.
# def doSignup(request):
#      try:
#          email = request.data['email']
#          password = request.data['password']
#      except:
#          return Response({'error': 'Please provide correct email and password'},
#                          status=HTTP_400_BAD_REQUEST)
#      user = authenticate(email=email, password=password)
#      if user is not None:
#          token, _ = Token.objects.get_or_create(user=user)
#          return Response({'authenticated': True, 'token': "Token " + token.key})
#      else:
#          return Response({'authenticated': False, 'token': None})
# def getSignup(request):
# 	#return render(request, 'signup.html')
# ####################################
# ###############Login################
# ####################################
def getLogin(request):
	return render(request, 'login.html')

@csrf_exempt
def doLogin(request):
	em = request.POST.get ('email')
	password = request.POST.get ('password')
	print(em)
	print(password)
	try:
		c=Customer.objects.get(email=em,password=password)
		request.session['customer'] = c.id
		request.session['cart'] = {}
		categories = Category.get_all_categories()
		return redirect('getProducts')
	except Exception as e:
		print(e)
		return render(request, 'login.html')

def doLogout(request):
    request.session.clear()
    return redirect('getLogin')		
	
# ####################################
# ###############Sign up################
# ####################################
# @csrf_exempt
# def doSignup(request):
# 	#check that user email doesn't exist first
# 	pass


from django.core.paginator import Paginator

def getProducts(request):
	categories = Category.get_all_categories()
	categoryID = request.GET.get('category')
	if categoryID:
		products = Products.get_all_products_by_categoryid(categoryID)
	else:
		products = Products.get_all_products();
	paginator = Paginator(products, 2) 
	page_number = request.GET.get('page')
	products = paginator.get_page(page_number)
	data = {}
	data['products'] = products
	data['categories'] = categories
	return render(request, 'products.html',data)
	
# @csrf_exempt	
# def updateCard(request):
# 	remove = request.POST.get('remove')
# 	pid=request.POST.get('product')
# 	cart = request.session.get('cart')
	
# 	if cart:
# 		print(cart.get(pid))
# 		quantity = cart.get(pid)
# 		if quantity:
# 			if remove:
# 				if quantity<=1:
# 					cart.pop(pid)
# 				else:
# 					cart[pid]  = quantity-1
# 			else:
# 				cart[pid]  = quantity+1
# 		else:
# 			cart[pid] = 1
# 	else:
# 		cart = {}
# 		cart[pid] = 1
# 	request.session['cart'] = cart
# 	print('cart' , request.session['cart'])
# 	return redirect('getProducts')
	
# def getCart(request):
#     ids = list(request.session.get('cart').keys())
#     products = Products.get_products_by_id(ids)
#     print(products)
#     return render(request , 'cart.html' , {'products' : products} )

# @csrf_exempt
# def checkOut(request):
# 	address = request.POST.get('address')
# 	phone = request.POST.get('phone')
# 	customer = request.session.get('customer')
# 	cart = request.session.get('cart')
# 	products = Products.get_products_by_id(list(cart.keys()))
# 	for product in products:
# 		order=Order(customer=Customer(id=customer),product=product,price=product.price, address=address,phone=phone,quantity=cart.get(str(product.id)))
# 		order.save()
# 	request.session.clear()
# 	return redirect('getLogin')	



# def getOrders( request ):
#     customer = request.session.get('customer')
#     orders = Order.get_orders_by_customer(customer)
#     return render(request , 'orders.html'  , {'orders' : orders})