from django.db import models

class Place(models.Model):
    place_name = models.CharField("название места", max_length=200)

class Comment(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    author = models.CharField("Имя автора", max_length= 50)
    comment_text = models.CharField("Текст комментария", max_length=200)
# Create your models here.
