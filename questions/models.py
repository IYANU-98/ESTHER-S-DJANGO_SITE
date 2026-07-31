from django.db import models

class PastQuestion(models.Model):  # 'models' must be lowercase
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20)
    year = models.IntegerField()
    question_text = models.TextField()  # Make sure 'TextField' has a capital T and F

    def __str__(self):
        return f"{self.course_code} ({self.year})"  # Make sure this has two underscores on each side of 'str'
