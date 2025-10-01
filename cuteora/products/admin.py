from django.contrib import admin
from .models import Product,Category,Message,Review,Cart,CartItem
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)