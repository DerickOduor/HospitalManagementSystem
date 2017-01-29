from django.db import models
from django.core.urlresolvers import reverse

class Student_Database(models.Model):
    Image = models.FileField()
    Registration_No = models.CharField(max_length=20)
    Name = models.CharField(max_length=40)
    Faculty = models.CharField(max_length=40)
    Department = models.CharField(max_length=40)
    Course = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.Registration_No + ' - ' + self.Name

class Records(models.Model):
    Student_Information = models.ForeignKey(Student_Database)
    Student_Name = models.CharField(max_length=40)
    Date = models.DateField()
    Problem = models.TextField(max_length=100)
    Prescription = models.TextField(max_length=200)
    Maternity_Services = models.TextField(max_length=100)
    Lab_Results = models.TextField(max_length=100)
    Ward_Report = models.TextField(max_length=100)
    
    def get_absolute_url(self):
        return reverse('success')

    def __str__(self):
        return self.Problem


