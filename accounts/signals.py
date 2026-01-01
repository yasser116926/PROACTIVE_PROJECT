from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile, UserRole

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        role = UserRole.STUDENT
        can_fly = False

        if instance.is_superuser:
            role = UserRole.ADMIN
            can_fly = True

        Profile.objects.create(
            user=instance,
            role=role,
            approved=(role != UserRole.STUDENT),
            can_access_flights=can_fly
        )
