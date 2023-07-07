import datetime
from rest_framework import serializers

from .models import (
    Category,
    CategoryIcon,
    Product,
    Tag,
    Review,
    ProductSpecification,
    Sale
)


class CategoryIconSerializer(serializers.ModelSerializer):
    """Сериализатор значков категорий"""

    class Meta:
        model = CategoryIcon
        fields = ["id", "src", "alt"]


class SubCategorySerializer(serializers.ModelSerializer):
    """Сериализатор подкатегорий"""

    class Meta:
        model = Category
        fields = "__all__"

    image = CategoryIconSerializer(many=False, read_only=True)


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категорий"""

    class Meta:
        model = Category
        fields = "__all__"

    image = CategoryIconSerializer(many=False, required=False)
    subcategories = SubCategorySerializer(many=True, required=False)


class ProductSpecificationSerializer(serializers.ModelSerializer):
    """Сериализатор спецификаций продуктов"""

    class Meta:
        model = ProductSpecification
        fields = ["id", "name", "value"]


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор отзывов"""

    class Meta:
        model = Review
        fields = ['author', 'email', 'text', 'rate', 'date', 'product']

    date = serializers.SerializerMethodField()

    def get_date(self, instance):
        date = instance.date + datetime.timedelta(hours=3)
        return datetime.datetime.strftime(date, '%d.%m.%Y %H:%M')


class TagsProductSerializer(serializers.ModelSerializer):
    """Сериализатор тегов"""

    class Meta:
        model = Tag
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор продуктов"""

    class Meta:
        model = Product
        fields = "__all__"

    images = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, required=False)
    tags = TagsProductSerializer(many=True, required=False)
    specifications = ProductSpecificationSerializer(many=True, required=False)
    price = serializers.SerializerMethodField()

    def get_images(self, instance):
        images = []
        images_tmp = instance.images.all()
        for image in images_tmp:
            images.append({"src": f"/media/{image.__str__()}", "alt": image.name})
        return images

    def get_price(self, instance):
        salePrice = instance.sales.first()
        if salePrice:
            instance.price = salePrice.salePrice
            instance.save()
            return salePrice.salePrice
        return instance.price


class SaleSerializer(serializers.ModelSerializer):
    """Сериализатор распродаж"""
    class Meta:
        model = Sale
        fields = '__all__'

    images = serializers.SerializerMethodField()
    title = serializers.StringRelatedField()
    href = serializers.StringRelatedField()
    price = serializers.StringRelatedField()
    dateFrom = serializers.DateField(format='%d.%b')
    dateTo = serializers.DateField(format='%d.%b')

    def get_images(self, instance):
        images = []
        images_tmp = instance.product.images.all()
        for image in images_tmp:
            images.append({"src": f"/media/{image.__str__()}", "alt": image.name})
        return images

