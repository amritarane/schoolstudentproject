from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    SchoolName=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.SchoolName
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Student(models.Model):
    StudentName=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    SchoolName=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    
    def __str__(self) -> str:
        return self.StudentName