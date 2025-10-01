from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100)
    image_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title=models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    stock = models.PositiveIntegerField()
    description =models.TextField(blank=False)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.product.price * self.quantity  # <-- compute dynamically
  
       

class Message(models.Model):
    name = models.CharField(max_length=100)  
    email = models.EmailField() 
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
    name = models.CharField(max_length=100) 
    review = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}⭐"    
