from unicodedata import category
from django.contrib import admin
from .models import Category,  Product, ProductGallery, Feedback, OrderFeedback

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductGallery)
admin.site.register(Feedback)
admin.site.register(OrderFeedback)

