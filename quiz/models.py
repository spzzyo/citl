from django.db import models
from courses.models import Course
# Create your models here.


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)




