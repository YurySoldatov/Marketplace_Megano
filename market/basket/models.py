from django.db import models


from catalog.models import Product
from accounts.models import Profile


class Order(models.Model):
    """
    Класс, описывающий модель заказа.
    """
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    products = models.ManyToManyField(Product, related_name='orders', verbose_name='Продукты')
    user = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='orders', verbose_name='Пользователь')
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=20, default='', verbose_name='Статус')
    deliveryType = models.CharField(max_length=20, default='', verbose_name='Тип доставки')
    paymentType = models.CharField(max_length=20, default='', verbose_name='Тип оплаты')
    totalCost = models.DecimalField(max_digits=10, default=0, decimal_places=2, verbose_name='Сумма заказа')
    city = models.CharField(max_length=20, default='', verbose_name='Город')
    address = models.CharField(max_length=200, default='', verbose_name='Адрес доставки')


class CountProductInOrder(models.Model):
    """
    Класс, описывающий модель количества товара в заказе.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Товар")
    count = models.PositiveIntegerField(verbose_name="Количество")

