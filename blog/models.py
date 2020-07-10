from django.db import models

# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateField(auto_now=False)
    description = models.CharField(max_length=600)
    image = models.ImageField(upload_to='blog/images')

    def __str__(self):
        return self.title
