from django.db import models

class PastQuestion(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20)
    year = models.IntegerField()
    question_text = models.TextField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='past_questions_pdfs/', blank=True, null=True)

    # <-- ADD THIS BRAND NEW CONFIGURATION BLOCK RIGHT HERE:
    class Meta:
        ordering = ['-year']  # The minus '-' means descending order (Newest to Oldest)

    def __str__(self):
        return f"{self.course_code} ({self.year})"
