from django.db import models

class UserProfile(models.Model):
    user_name = models.CharField(max_length=250)
    user_contact = models.CharField(max_length=13)
    