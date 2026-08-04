from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True) # e.g., "Faculty of Science"

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100) # e.g., "Computer Science"
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return f"{self.name} ({self.faculty.name})"

class PastQuestion(models.Model):
    # Semester choices
    SEMESTER_CHOICES = [
        ('FIRST', 'First Semester'),
        ('SECOND', 'Second Semester'),
    ]

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='questions')
    course_name = models.CharField(max_length=200)  # e.g., "Introduction to Programming"
    course_code = models.CharField(max_length=20)   # e.g., "CSC 101"
    section = models.CharField(max_length=50) 
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    year = models.IntegerField()                    
    
    # Core contents
    question_text = models.TextField(blank=True, null=True)
    answer_text = models.TextField(blank=True, null=True) # <-- Added Answer Entity row!
    pdf_file = models.FileField(upload_to='past_questions_pdfs/', blank=True, null=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return f"{self.course_code} - {self.semester} ({self.year})"
