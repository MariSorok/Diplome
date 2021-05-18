import time
from django.contrib.auth.models import AnonymousUser

from django.db import models
from datetime import timedelta, datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

def generate_imageset_upload_to(instance, filename=None):
    return f'images/{instance.id}_{str(int(time.time()))}.png'

class Table(models.Model):
    number = models.PositiveIntegerField()
    seats_num = models.PositiveIntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'


class Dish(models.Model):
    SNAKS = 'SNA'
    HOT = 'HOT'
    DRINKS = 'DRI'
    SWEETS = 'SWE'
    SALADS = 'SAL'
    DISH_CATYGORY_CHOICES = [
        (SNAKS, 'Закуски'),
        (HOT, 'Горяие блюда'),
        (DRINKS, 'Напитки'),
        (SWEETS, 'Десерты'),
        (SALADS, 'Салаты'),
    ]
    category = models.CharField(
        max_length=3,
        choices=DISH_CATYGORY_CHOICES,
        default=HOT
    )
    name = models.CharField(max_length=255, verbose_name="Название блюда")
    description = models.CharField(max_length=1023, blank=True, null=True, verbose_name="Описание блюда")
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to=generate_imageset_upload_to, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class Preorder(models.Model):
    number = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    dishes = models.CharField(max_length=255, default="Предварительный заказ отсутствует.", verbose_name="Блюда")

    class Meta:
        verbose_name = 'Предзаказ'
        verbose_name_plural = 'Предзаказы'


class Booking(models.Model):
    WAITING = 'WA'
    ACCEPTED = 'AC'
    REJECTED = 'RE'
    BOOKING_STATUS_CHOICES = [
        (WAITING, 'В ожидании'),
        (ACCEPTED, 'Подтверждено'),
        (REJECTED, 'Отклонено'),
    ]
    persons_num = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name="количество человек")
    booked_at = models.DateTimeField(default=datetime.now)
    # duration = models.DurationField(default=timedelta(minutes=20))
    status = models.CharField(
        max_length=2,
        choices=BOOKING_STATUS_CHOICES,
        default=WAITING
    )
    closed = models.BooleanField(default=False, verbose_name="Бронь закрыта?")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь, создавший бронь")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="Стол")
    preorder = models.ForeignKey(Preorder, on_delete=models.CASCADE, verbose_name="Предзаказ")

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'