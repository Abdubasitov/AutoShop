from django.db import models
from django.contrib.auth import get_user_model
from apps.product.models import ProductVariant

User = get_user_model()


class Order(models.Model):
    STATUS_CHOICE=(
        ('new', 'Новый'),
        ('processing', 'В процессе'),
        ('completed', 'Завершенный'),
        ('cancaled', 'Отменен'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICE, default='new'
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Заказ: {self.id}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items'
    )
    variant = models.ForeignKey(
        ProductVariant, on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quanity = models.PositiveIntegerField()
    
    def __str__(self):
        return self.variant.product.name
    
    
class ShippingAddress(models.Model):
    Order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name='shipping',
        verbose_name="Адрус доставки"
    )
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=150)
    addres = models.TextField()
    
    def __str__(self):
        return self.full_name
    
    
class Payment(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name='payment'
    )
    method = models.CharField(max_length=10)
    is_paid = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.method