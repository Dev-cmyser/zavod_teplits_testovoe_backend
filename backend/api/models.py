from django.db import models
from ckeditor.fields import RichTextField
import uuid
from versatileimagefield.fields import VersatileImageField


class BaseModel(models.Model):
    """Basic Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class BaseImage(models.Model):
    """Basic model for images"""
    title = models.CharField(max_length=200, null=True, blank=True)
    alt = models.CharField(max_length=200, null=True, blank=True)
    image = VersatileImageField(null=True, blank=True, upload_to='images')

    class Meta:
        abstract = True
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        res = ''
        if self.title:
            res = self.title
        else:
            res = self.image.url
        return res




class Product(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Имя')
    price = models.IntegerField(verbose_name='Цена')
    count = models.IntegerField(verbose_name='Количество')
    is_active = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductImage(BaseImage):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продуктов'

class City(BaseModel):
    name = models.CharField(max_length=254, verbose_name='Имя')
    phone_number = models.CharField(max_length=25, verbose_name='Номер')
    photo = models.ImageField(upload_to='media/city', max_length=254, verbose_name='Фото', blank=True, null=True)
    map_x = models.FloatField(max_length=254, verbose_name='Координатa x')
    map_y = models.FloatField(max_length=254, verbose_name='Координата y')
    is_active = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Feedback(BaseModel):
    name = models.CharField(max_length=254, verbose_name='Имя')
    message = models.TextField( verbose_name='Отзыв')
    photo = models.ImageField(upload_to='media/persons', max_length=254, verbose_name='Фото', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class FeedbackImage(BaseImage):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Изображение отзыва'
        verbose_name_plural = 'Изображения отзывов'