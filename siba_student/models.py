from django.db import models
from siba_admin.models import Courses

class student_db(models.Model):
    # radio button values
    RADIO_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
    ]

    student_Id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=RADIO_CHOICES)

    def __str__(self):
        return self.student_Id + " " + " - " + " " + self.name
