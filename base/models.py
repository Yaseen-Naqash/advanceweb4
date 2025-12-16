from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    SIZES = [
        ('0','M'),
        ('1','L'),
        ('2','XL'),
        ('3','XXL'),
    ]


    title = models.CharField(max_length=127, null=True, verbose_name='عنوان')
    price = models.DecimalField(max_digits=6, null=True, decimal_places=2, verbose_name='قیمت')
    size = models.CharField(max_length=1, null=True, choices=SIZES, verbose_name='سایز')
    description = models.TextField(max_length=2047, null=True, verbose_name='توضیحات')
    static_discount = models.DecimalField(max_digits=4, null=True, decimal_places=2, verbose_name='قیمت تخفیف', blank=True)
    percent_dicount = models.IntegerField(null=True, blank=True)

    product_features = models.ManyToManyField('ProductFeature')
    image = models.ImageField(upload_to='Product_images/', null=True, default='store.png')
    
    def __str__(self):
        return self.title
    
    @property
    def final_price(self):
        if self.static_discount:
            return self.price - self.static_discount
        elif self.percent_dicount:
            return self.price * (1 - self.percent_dicount/100)
        else:
            return self.price

         

class ProductFeature(models.Model):
    name = models.CharField(max_length=127, null=True, verbose_name='ویژگی')

    def __str__(self):
        return self.name


class Comment(models.Model):
    SUGGESTION = [
        ('0','I suggest this Product'),
        ('1',"I don't suggest this Product"),
        ('2','I have no idea.'),
    ]

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='نویسنده')
    body = models.TextField(max_length=2047, null=True, verbose_name='متن')
    suggestion = models.CharField(max_length=1, choices=SUGGESTION, null=True, verbose_name='خلاصه')

    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, verbose_name='محصول')

    def __str__(self):
        return self.body[:50]
    
