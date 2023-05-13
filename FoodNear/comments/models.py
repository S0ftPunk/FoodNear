from django.db import models

class Place(models.Model):
    place_name = models.CharField("название места", max_length=200)
    place_adres = models.CharField("адрес места", max_length=200)
    place_pic = models.ImageField("Фотка", upload_to='images/')
    def __str__(self):
        return  self.place_name

class Comment(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    author = models.CharField("Имя автора", max_length= 50)
    comment_text = models.CharField("Текст комментария", max_length=200)
    def __str__(self):
        return  f"{self.author, self.place}"
class Picture(models.Model):
    image = models.ImageField("Фотка", upload_to='images/')
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    def __str__(self):
        return  self.place.place_name
# Create your models here.
