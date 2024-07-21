from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='shop/category/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Shop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=200)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='shop/shop/', null=True)
    price = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Shop_Detail(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=200)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='shop/shop_detail/', null=True)
    price = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title