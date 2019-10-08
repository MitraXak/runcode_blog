from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
# models.Model - так django поймет, что эту модель надо сохранить в БД
class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	publish_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title

