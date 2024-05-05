from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=1000)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()
# Create your models here.
class Car(models.Model):
    carname= models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def _str_(self) -> str:
        return self.carname