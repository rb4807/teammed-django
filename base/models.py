from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_des = models.TextField()
 
class Doctor(models.Model) :
    name = models.CharField(max_length=100)
    dep = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Doctors')

    def __str__(self):
        return 'Dr ' + self.name + ' - (' + self.dep + ')'
    

class Booking(models.Model) :
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    booked = models.DateField()
