from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
	img = models.ImageField(upload_to='images/')
	summary = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)

