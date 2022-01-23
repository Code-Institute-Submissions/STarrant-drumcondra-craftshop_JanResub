from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    '''
    User profile model for holding personal details,
    delivery information and contact details and order history.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_phone_no = models.CharField(max_length=20, null=True, blank=True)
    default_address_street_1 = models.CharField(max_length=80,
                                                null=True, blank=True)
    default_address_street_2 = models.CharField(max_length=80,
                                                null=True, blank=True)
    default_address_town_city = models.CharField(max_length=40,
                                                 null=True, blank=True)
    default_address_postcode = models.CharField(max_length=20,
                                                null=True, blank=True)
    default_address_country = CountryField(null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    '''
    Create or update a user profile.
    '''
    # Creating a new user.
    if created:
        UserProfile.objects.create(user=instance)
    # Updating an existing user.
    instance.userprofile.save()
