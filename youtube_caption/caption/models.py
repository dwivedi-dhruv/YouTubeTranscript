from django.db import models

# Create your models here.

class transcriptModel(models.Model):
    videoID = models.CharField(max_length=100)
    transcript = models.TextField()

    def __str__(self):
        return str(self.id)