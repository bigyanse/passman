from django.db import models

# Create your models here.
class SavedPassword(models.Model):
	site = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)