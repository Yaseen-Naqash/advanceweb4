from django.db import models

# Create your models here.
class Book(models.Model):

    LANGUAGES = [
        ('0','farsi'),
        ('1','arabic'),
        ('2','english'),
    ]


    title = models.CharField(max_length=127, null=True ,default='test')
    description = models.TextField(max_length=2047, null=True, blank=True)
    price = models.IntegerField(default=99)
    publisher = models.CharField(max_length=127, null=True)
    is_released = models.BooleanField( default=True)
    release_date = models.DateField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    language = models.CharField(max_length=1, choices=LANGUAGES)

    writer = models.ForeignKey('Writer',on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField('Category')




class Writer(models.Model):
    first_name = models.CharField(max_length=127, null=True)
    last_name = models.CharField(max_length=127, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Category(models.Model):
    name = models.CharField(max_length=127, null=True)

    def __str__(self):
        return self.name