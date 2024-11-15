from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=50)
    image=models.ImageField(upload_to="category")
    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=50)
    image=models.ImageField(upload_to="product")
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
