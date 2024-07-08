from django.db import models
from django.contrib.auth import get_user_model
class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)


    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name


class product(models.Model):
    category = models.ManyToManyField(Category, related_name='product')
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='ProductMedia/%Y/%M')
    description = models.TextField()
    price = models.IntegerField()
    rate = models.FloatField()
    available = models.BooleanField(default=True)
    creation = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


    class Meta:
        ordering =('name', )

    def __str__(self):
        return self.name