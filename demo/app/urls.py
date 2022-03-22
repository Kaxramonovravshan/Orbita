from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('product-detail/<int:id>/', views.product_detail, name='product_detail'),
    path('category-detail/<int:id>/', views.category_detail, name='category_detail'),
    path('feedback/', views.feedback, name='feedback'),
    path('orderfeedback/<int:id>/', views.order_feedback, name='order_feedback'),
    path('product-detail/<int:id>/', views.product_detail, name ='product_detail'),
    path('templ/', views.templ, name ='templ'),

        
    
]
