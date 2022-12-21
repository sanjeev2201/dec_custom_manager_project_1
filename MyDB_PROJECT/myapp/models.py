from django.db import models

# Create Student models here.
class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    student_manager = models.Manager()

    class Meta:
        db_table = 'Student'
        ordering = ['roll_no']

#create Proxy_Student models here

class Proxy_Student(Student):
    class Meta:
        proxy = True
        proxy_manager = models.Manager()
        db_table = 'Proxy_Student'
        ordering = ['name']


        