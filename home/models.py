from django.db import models
from django.urls import reverse

STATUS = (('active','active'),('','default'))
LABEL = (('new','new'),('hot','hot'),('sale','sale'),('default','default'))
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 200)
    image = models.CharField(max_length=200,null=True)
    slug = models.CharField(max_length=100,unique= True)
    status =  models.CharField(choices= STATUS, max_length= 200)

    def __str__(self):
        return  self.name

class Slider(models.Model):
    name = models.CharField(max_length= 300)
    image = models.ImageField(upload_to= 'media',null=True)
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS, max_length=200)


    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length= 200)
    rank = models.IntegerField()
    image = models.ImageField(upload_to ='media',null=True)
    description = models.TextField(blank= True)
    status = models.CharField(choices=STATUS, max_length=200)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length= 200)
    image = models.ImageField(upload_to='media',null=True)
    status = models.CharField(choices=STATUS, max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default= 0)
    label = models.CharField(choices=LABEL, max_length= 200)
    image = models.ImageField(upload_to='media',null=True)
    status = models.CharField(choices=STATUS, max_length=200)
    slug = models.CharField(max_length= 200,unique= True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_item_url(self):
        return reverse("home:products",kwargs = {'slug':self.slug})

