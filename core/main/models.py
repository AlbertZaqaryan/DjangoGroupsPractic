from django.db import models
# Create your models here.

# Ստեղծում ենք մի քանի մոդելներ և հետո բոլորը միացնում ենք 1 views ին
class HomeSlide(models.Model):
    name = models.CharField('Slide name', max_length=30)
    about = models.TextField('Slide about')
    img = models.ImageField('Smilde image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeSlide'
        verbose_name_plural = 'HomeSlides'

class HomeProduct(models.Model):
    name = models.CharField('Product name', max_length=30)
    about = models.TextField('Product about')
    price = models.IntegerField('Product price')
    img = models.ImageField('Product image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeProduct'
        verbose_name_plural = 'HomeProducts'

