from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class Book(models.Model):
    LANGUAGES = [
        ('0','farsi'),
        ('1','arabic'),
        ('2','english'),
    ]
    title = models.CharField(max_length=127, null=True,default='test', verbose_name='نام')
    description = models.TextField(max_length=2047, null=True, blank=True, verbose_name='توضیحات')
    price = models.IntegerField(default=99, verbose_name='قیمت')
    rate = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=0.00, verbose_name='امتیاز')
    publisher = models.CharField(max_length=127, null=True, blank=True, verbose_name='ناشر')
    is_released = models.BooleanField( default=True, blank=True, verbose_name='انتشار')
    release_date = jmodels.jDateField(null=True, blank=True, verbose_name='تاریخ انتشار')
    created_at = models.DateTimeField(null=True, auto_now_add=True, verbose_name='تاریخ ساخت')
    updated_at = models.DateTimeField(null=True, auto_now=True, verbose_name='تاریخ آپدیت')
    language = models.CharField(max_length=1, choices=LANGUAGES, default='0', verbose_name='زبان')
    writer = models.ForeignKey('Writer',on_delete=models.SET_NULL, null=True, blank=True, verbose_name='نویسنده')
    categories = models.ManyToManyField('Category', blank=True, verbose_name='دسته بمدی')

    def __str__(self):
        return self.title


class Writer(models.Model):
    first_name = models.CharField(max_length=127, null=True)
    last_name = models.CharField(max_length=127, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Category(models.Model):
    name = models.CharField(max_length=127, null=True)

    def __str__(self):
        return self.name