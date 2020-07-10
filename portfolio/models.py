from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=60)
    descriptions = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
