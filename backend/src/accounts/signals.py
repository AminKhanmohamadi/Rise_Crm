from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import  Customer , CustomUser


@receiver(post_save, sender=CustomUser)
def create_customer(sender, instance, created, **kwargs):
    if created:
        fullname = f'{instance.first_name} {instance.last_name}'.strip() or instance.email.split('@')[0]
        Customer.objects.create(owner=instance, name=fullname)