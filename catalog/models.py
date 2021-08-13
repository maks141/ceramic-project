from re import T
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.db.models.lookups import GreaterThan

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя категории')
    slug = models.SlugField(unique=True, verbose_name='Текст для ссылки (введите название товара на английском)')
    image = models.ImageField(upload_to='catalog/images' ,verbose_name='Изображение категории', null=True)
    add_in_home = models.BooleanField(verbose_name='Добавить эту категорию на главную страницу?', null=True)
    add_in_partners = models.BooleanField(verbose_name='Добавить эту категорию на cтраницу для пратнеров?', null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='catalog/images', verbose_name='Изображение товара', null=True)
    title = models.CharField(max_length=250, verbose_name='Имя товара')
    size = models.CharField(max_length=250, verbose_name='Размеры товара', null=True)
    descriprion = models.TextField(verbose_name='Описание товара', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    slug = models.SlugField(unique=True, verbose_name='Текст для ссылки (введите название товара на английском)')

    def __str__(self):
        return self.title


# class CartProduct(models.Model):
#     user = models.ForeignKey('Castomer', verbose_name='Покупатель', on_delete=models.CASCADE)
#     cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
#     qty = models.PositiveIntegerField(default=1)
#     final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

#     def __str__(self):
#         return 'CartProduct'

# class Castomer(models.Model):
#     user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

#     def __str__(self):
#         return (self.user.firt_name, self.user.last_name)

