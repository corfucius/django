from django.db import models
from datetime import datetime

# Create your models here.
#add migrations when you change this
#creates models that can be uploaded to db with manage.py makemigration and migrate
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.FileField(null=True, blank=True) 
    #or models.ImageField(default="default.png, blank=True")
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Posts"