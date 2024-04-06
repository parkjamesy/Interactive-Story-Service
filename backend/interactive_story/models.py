from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    text = models.TextField()

def _str_(self):
    return self.title
