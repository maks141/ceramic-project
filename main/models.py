from django.db import models
from django.db.models.fields.files import ImageField

class Slider(models.Model):
    image = models.ImageField(upload_to='catalog/images', verbose_name='Картинка для слайдера')

class NumberOrder(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=250)

class Partner(models.Model):
    text = models.TextField(verbose_name='Текст для партнеров')
    file = models.FileField(verbose_name='Файл для партеров')
    image = models.ImageField(upload_to='catalog/images', verbose_name='Фото для партнеров', null=True)

class About(models.Model):
    image = models.ImageField(upload_to='catalog/images', verbose_name='Фото для статьи', null=True)
    text = models.TextField(verbose_name='Текст статьи')
    
