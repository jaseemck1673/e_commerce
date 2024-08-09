from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.views import *

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    
    class Meta:
        ordering=('name',)
        verbose_name="category"
        verbose_name_plural="categories"
    
    def get_url(self):
        return reverse("prod_cat", args=[self.slug])
    
    def __str__(self):
        return '{}'.format(self.name)

class products(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(unique=True, blank=True, null=True)
    image=models.ImageField(upload_to='product')
    description=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category_id=models.ForeignKey(category,on_delete=models.CASCADE)
    
    def get_url(self):
        return reverse('details',args=[self.category_id.slug,self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save( *args, **kwargs)
        
        
    
    def __str__(self):
        return self.name
    
    