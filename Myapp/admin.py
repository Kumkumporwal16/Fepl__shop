from django.contrib import admin

# Register your models here.
from .models import Category,Product,CartItem,SubCategory

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(SubCategory)
