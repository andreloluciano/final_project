from django.db.models.signals import post_save
from django.contrib.auth.models import User #sender
from django.dispatch import receiver
from .models import Profile 


#esto es para crear un perfil con cada usuario creado
                         #User=Sender
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): #Reciever
    if created:
        Profile.objects.create(user=instance)

#guarda el perfil cada vez que el User es .save
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

    