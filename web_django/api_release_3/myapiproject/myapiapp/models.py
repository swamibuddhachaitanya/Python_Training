from django.db import models

# Create your models here.

class MyModel(models.Model):
    course = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.course

    class Meta:
        db_table = 'my_course_table'


