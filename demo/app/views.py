from itertools import product
from math import prod
from django import http
from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm
from . models import Category, Feedback, Product,OrderFeedback
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from users.forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt

def index(request):  
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'pages/index.html', {'categories':categories,'products':products})
    


def templ(request):  
    return render(request, 'pages/templ.html')



# category-detail
def category_detail(request, id):   
    category = Category.objects.get(id=id)
    return render(request, 'pages/category-detail.html', {'category':category})
    


# product-detail
def product_detail(request, id):
    product = Product.objects.get(id = id)
    return render(request, 'pages/product-detail.html', {'product':product})




def feedback(request):
    number = request.POST.get('number')
    name = request.POST.get('name')
    feedback = Feedback()
    feedback.number = number
    feedback.name = name
    feedback.save()
    return render(request, 'pages/success.html')
    



def order_feedback(request, id):
    product = Product.objects.get(id=id)
    number = request.POST.get('number_')
    name = request.POST.get('name_')
    email = request.POST.get('email')
    feedback = OrderFeedback()
    feedback.product = product
    feedback.number = number
    feedback.name = name
    feedback.email = email
    feedback.save()
    return render(request, 'pages/success.html')
    


