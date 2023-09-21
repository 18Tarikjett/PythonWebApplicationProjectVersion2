from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


#The information received to create and save a profile after user is registered is automatically done through the create_profile function()
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


#Any changes are also saved to a created profile through the save_profile() function
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()