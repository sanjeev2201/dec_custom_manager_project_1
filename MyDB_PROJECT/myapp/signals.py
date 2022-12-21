# code
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student,Proxy_Student


@receiver(post_save, sender=Student)
def create_profile(sender, instance, created, **kwargs):
    print("sender:",sender)
    print('instance:',instance)
    if created:
        print("new student record save")

@receiver(post_save, sender=Proxy_Student)
def save_profile(sender, instance,created,**kwargs):
    print("sender:",sender)
    print('instance:',instance)
    if created:
        print("new  proxy student record save")
