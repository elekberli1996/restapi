from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    content=models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
