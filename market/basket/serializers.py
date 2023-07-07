import datetime
from decimal import Decimal
from rest_framework import serializers

from catalog.serializers import ProductSerializer
from catalog.models import Product
from .models import Order


class BasketSerializer(serializers.ModelSerializer):
    """Сериализатор корзины продуктов"""

    count = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_count(self, obj):
        return self.context.get(str(obj.pk)).get('count')

    def get_price(self, obj):
        return Decimal(self.context.get(str(obj.pk)).get('price'))

    def get_images(self, instance):
        images = []
        images_tmp = instance.images.all()
        for image in images_tmp:
            images.append({"src": f"/media{image.__str__()}", "alt": image.name})
        return images


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор заказа"""

    class Meta:
        model = Order
        fields = '__all__'

    products = ProductSerializer(many=True, required=True)
    fullName = serializers.StringRelatedField()
    email = serializers.StringRelatedField()
    phone = serializers.StringRelatedField()
    createdAt = serializers.SerializerMethodField()

    def get_createdAt(self, instance):
        date = instance.createdAt + datetime.timedelta(hours=3)
        return datetime.datetime.strftime(date, '%d.%m.%Y %H:%M')
