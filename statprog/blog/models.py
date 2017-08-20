from django.db import models

# Create your models here.


class Category(models.Model):
	title=models.CharField(max_length=100,unique=True)
	banner_ref = models.CharField(max_length=200)
	num = models.IntegerField()

class Blog(models.Model):
	title=models.CharField(max_length=100, unique=True)
	description = models.CharField(max_length=200, unique=True)
	body=models.TextField()
	post_num=models.IntegerField()
	post_date=models.DateField(db_index=True,auto_now_add=True)
	thumbnail_reference=models.CharField(max_length=200) # local reference
	site_url=models.CharField(max_length=200)
	category=models.ForeignKey('blog.Category')
	topics=models.ManyToManyField('blog.Topic')

class Topic(models.Model):
	name=models.CharField(max_length=100)
