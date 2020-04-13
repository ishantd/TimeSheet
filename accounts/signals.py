from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Employee


@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
        print("PROFILE CREATED!")
    instance.employee.save()
    print("Profile saved with details")
        
@receiver(post_save, sender=User)
def update_employee(sender, instance, created, **kwargs):
    if created==False:
        instance.employee.save()
        print("PROFILE Updated!")