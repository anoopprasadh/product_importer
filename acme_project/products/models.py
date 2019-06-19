from django.db import models
import numpy as np

# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length=264)
	sku = models.CharField(max_length=264)
	description = models.TextField()
	status = models.CharField(max_length=264,default='Active')

	def __str__(self):
		return self.name


