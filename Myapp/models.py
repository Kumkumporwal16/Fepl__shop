from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    category = models.ForeignKey(Category,related_name='subcategories',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
   
    def __str__(self):
        return self.name

class Product (models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    subCategory = models.ForeignKey(SubCategory,related_name="products",on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200)   
    slug=models.SlugField(unique=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='products/')
    stock=models.PositiveIntegerField(default=0)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name

'''class ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name="images",on_delete=models.CASCADE )
    image = models.ImageField(upload_to='products/')
    thumbnail = models.BooleanField(default=False)

    def __str__(self):
        return self.name

'''

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)



