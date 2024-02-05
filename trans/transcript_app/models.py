from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    given_names = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10)
    registration_number = models.CharField(max_length=20)
    date_of_admission = models.DateField()
    date_of_graduation = models.DateField()
    award_title = models.CharField(max_length=255)
    classification_of_awards = models.CharField(max_length=50)
    overall_gpa = models.FloatField()

class Grade(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    module_name = models.CharField(max_length=255)
    grade = models.CharField(max_length=5)