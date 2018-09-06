from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=50)
	body = models.TextField()
	pub_date = models.DateField()
	img = models.ImageField(upload_to='images/')
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

