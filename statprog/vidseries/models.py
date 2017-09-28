from django.db import models

# Create your models here.
class Series(models.Model):
	series_title = models.CharField(max_length=50)
	series_subtitle = models.CharField(max_length=50)
	series_banner_ref = models.CharField(max_length=200)
	series_num = models.IntegerField()

	def __str__(self):
		return self.series_title

class Video(models.Model):
	title = models.CharField(max_length=50)
	prog_language = models.CharField(max_length=50)
	yt_reference = models.CharField(max_length=200) # url reference
	thumbnail_reference = models.CharField(max_length=200) # local reference
	lesson_num = models.IntegerField()
	post_date = models.DateField()
	site_url = models.CharField(max_length=200)
	series_id = models.ForeignKey(Series, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

