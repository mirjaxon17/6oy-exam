from django.db import models
from .helpers import SaveMediaFiles, Choises



class Types(models.Model):
    types = models.CharField(max_length=40)
    image = models.ImageField(upload_to=SaveMediaFiles.type_image_path)

    def __str__(self):
        return self.types
    



class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    types = models.ManyToManyField(Types)
    price = models.FloatField()
    image = models.ImageField(upload_to=SaveMediaFiles.product_image_path)
    price_type = models.CharField(max_length=10, choices=Choises.PriceType.choices, default=Choises.PriceType.sum)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def allproduct(self):
        all = len(self.title)
        return all
    def product_type(self):
        pr = self.types
        return pr
    def __str__(self):
        return self.title
    

class Bonus(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to=SaveMediaFiles.bonus_image_path)
    discount = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    price_type = models.CharField(max_length=15, choices=Choises.PriceType.choices, default=Choises.PriceType.s)
    fitured_price = models.FloatField(null=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Organic(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFiles.organic_image_path)
    types = models.ManyToManyField(Types) 
    price = models.FloatField()
    price_type = models.CharField(max_length=10, choices=Choises.PriceType.choices, default=Choises.PriceType.sum)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    def product_type(self):
        pr = self.types
        return pr


class Testiminial(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to=SaveMediaFiles.testiminal_image_path)
    description = models.TextField()
    profession = models.CharField(default='Yemit')
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.first_name}"



     

