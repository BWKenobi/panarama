from django.db import models

class ThetaImage(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=80)
	summary = models.CharField(max_length=200)