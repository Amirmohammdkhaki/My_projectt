from django .db import models


class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.PositiveIntegerField(default=0)
    active=models.BooleanField(default=True)
    cover=models.ImageField()

    datetime_create=models.DateTimeField(auto_now_add=True)
    datatime_modified=models.DateTimeField(auto_now=True)