from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=128,unique=True)
    descprition = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    description =  models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quanitity = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f'Продукт: {self.name} |Категория: {self.category.name}'
    



