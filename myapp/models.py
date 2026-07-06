from django.db import models

class Course(models.Model):
    course=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)

    def __str__(self):
        return self.course

class Student(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    age=models.IntegerField()
    roll_no=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)