from django.db import models

# Create your models here.
class user(models.Model):
    FirstName = models.CharField(max_length=264)
    LastName = models.CharField(max_length=264)
    Email= models.EmailField(max_length=70,unique=True)

    def __str__(self):
        return self.FirstName
