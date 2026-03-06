from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="teachers/",blank=True,null=True)

    def __str__(self):
      return self.name

class Students(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=20)
    DOB = models.DateField()
    contact = models.CharField(max_length=15)
    image = models.ImageField(upload_to="students/",blank=True,null=True)

    def __str__(self):
        return self.name


