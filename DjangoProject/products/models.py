from django.db import models
from users.models import User
# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Продукт'
        verbose_name_plural='Продукты'

    def __str__(self):
        return self.name

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)
    def total_quantity(self):
        return sum(basket.quantity for basket in self)

class Basket(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    product = models.ForeignKey(Product,models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects  = BasketQuerySet.as_manager()

    def __str__(self):
        return f'{self.user.email}|{self.product.name}'

    def sum(self):
        return self.product.price * self.quantity