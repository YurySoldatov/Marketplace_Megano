from django.db import models


def category_image_directory_path(instance: "CategoryIcon", filename):

    if instance.category.parent:
        return f"catalog/icons/{instance.category.parent}/{instance.category}/{filename}"
    else:
        return f"catalog/icons/{instance.category}/{filename}"


def product_image_directory_path(instanse: "ProductImage", filename):
    return f"products/images/{instanse.product.pk}/{filename}"


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["pk"]

    title = models.CharField(max_length=128, db_index=True, verbose_name="Название")
    active = models.BooleanField(default=False, verbose_name="Активна")
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="subcategories",
        verbose_name="Надкатегории"
    )
    favourite = models.BooleanField(default=False)


class CategoryIcon(models.Model):
    class Meta:
        verbose_name = "Значок категории"
        verbose_name_plural = "Значки категорий"
        ordering = ["pk"]

    source = models.FileField(
        upload_to=category_image_directory_path,
        max_length=500,
        verbose_name="Путь к файлу"
    )
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
        related_name="image",
        blank=True,
        null=True,
        verbose_name="Категория"
    )


class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["pk"]

    title = models.CharField(max_length=128, null=False, blank=False, verbose_name="Название")
    description = models.CharField(max_length=256, null=False, blank=True, verbose_name="Краткое описание")
    fullDescription = models.TextField(null=False, blank=True, verbose_name="Подробное описание")
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, null=False, verbose_name="Цена")
    count = models.IntegerField(default=0, null=False, verbose_name="Количество")
    date = models.DateTimeField(auto_now_add=True, null=False, verbose_name="Дата создания")
    freeDelivery = models.BooleanField(default=True, verbose_name="Бесплатная доставка")
    limited_edition = models.BooleanField(default=False, verbose_name="Количество ограничено")
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=2, null=False, verbose_name="Рейтинг")
    active = models.BooleanField(default=False, verbose_name="Активно")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products',
        verbose_name="Категория"
    )

    def __str__(self):
        return self.title


class ProductSpecification(models.Model):
    class Meta:
        verbose_name = "Спецификация товара"
        verbose_name_plural = "Спецификации товара"

    name = models.CharField(max_length=256, default="", verbose_name="Название")
    value = models.CharField(max_length=256, default="", verbose_name="Значение")
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="specifications",
        verbose_name="Товар"
    )


class ProductImage(models.Model):
    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товара"
        ordering = ["pk"]

    name = models.CharField(max_length=128, null=False, blank=True)
    image = models.FileField(upload_to=product_image_directory_path)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Товар"
    )


class Tag(models.Model):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["pk"]

    name = models.CharField(max_length=128, null=False, blank=True)
    product = models.ManyToManyField(Product, related_name="tags", verbose_name="Товар")

    def __str__(self):
        return self.name


class Review(models.Model):
    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        ordering = ["pk"]

    author = models.CharField(max_length=128, verbose_name="Автор")
    email = models.EmailField(max_length=256, verbose_name="Email")
    text = models.TextField(verbose_name="Комментарий")
    rate = models.PositiveSmallIntegerField(blank=False, default=5, verbose_name="Оценка")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="reviews", verbose_name="Товар")

    def __str__(self):
        return f"{self.author}: {self.product.title}"


class Sale(models.Model):
    class Meta:
        verbose_name = 'Распродажа'
        verbose_name_plural = 'Распродажи'

    salePrice = models.DecimalField(
        max_digits=10,
        db_index=True,
        decimal_places=2,
        default=0,
        verbose_name="Цена по акции"
    )
    dateFrom = models.DateField(default='')
    dateTo = models.DateField(blank=True, null=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='sales',
        verbose_name="Товар"
    )
