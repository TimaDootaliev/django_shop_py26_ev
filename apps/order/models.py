from django.db import models
from django.contrib.auth import get_user_model

from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import send_confirmation_mail


class OrderStatus(models.TextChoices):
    opened = 'opened'
    in_process = 'in_process'
    completed = 'completed'
    canceled = 'canceled'


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=OrderStatus.choices, default=OrderStatus.opened)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Order #{self.pk}"
    
    class Meta:
        verbose_name = 'Информация о заказе'
        verbose_name_plural = 'Информация о заказах'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveSmallIntegerField(default=1)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.product.title

    def save(self, *args, **kwargs):
        self.total_cost = self.quantity * self.product.price
        return super().save(self, *args, **kwargs)
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


@receiver(post_save, sender=Order)
def send_order_confirmation_mail(sender: Order, instance: Order, created: bool, **kwargs):
    if created:
        send_confirmation_mail(instance)