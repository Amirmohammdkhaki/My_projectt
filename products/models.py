from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    description = models.TextField()

    price = models.PositiveIntegerField(default=0)
    discount_price = models.PositiveIntegerField(default=0)

    stock = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    cover = models.ImageField(upload_to='products/')

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title