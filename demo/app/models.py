
import numbers
from pyexpat import model
from django.utils import timezone
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL



class Category(models.Model):
    title = models.CharField('Категория товара', max_length=256)
    icon = models.ImageField('Иконка', upload_to='category_icons', blank=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title






class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='category_products')
    title = models.CharField('Название товара', max_length=256)
    content = models.TextField('Контент', null=True)
    body = models.TextField('Описание', blank=True)
    image = models.ImageField('Фото', upload_to='product_image', blank=True)
    



    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


    



class ProductGallery(models.Model):
    image = models.ImageField('Image', upload_to='productColor gallery', blank=True)
    product = models.ForeignKey(Product, verbose_name='product', null=True, on_delete=models.CASCADE,blank=True)

    class Meta:
        verbose_name = 'ProductGallery'
        verbose_name_plural = 'ProductGallery'

    def __str__(self):
        return self.product.title




class OrderFeedback(models.Model):
    product = models.ForeignKey(Product, verbose_name='Order', null=True, on_delete=models.CASCADE,blank=True )
    number = models.CharField('Number', max_length=256)
    name = models.CharField('Name',max_length=256)
    email = models.EmailField('E-mail')
    data = models.DateTimeField('Data', default=timezone.now())


    class Meta:
        verbose_name = 'OrderFeedback'
        verbose_name_plural = 'OrderFeedback'

    def __str__(self):
        return self.name





class Feedback(models.Model):
    number = models.CharField('Number', max_length=256)
    name = models.CharField('Name',max_length=256)


    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'

    def __str__(self):
        return self.name






