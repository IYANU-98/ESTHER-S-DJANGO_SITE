from django.contrib import admin
from .models import Faculty, Department, PastQuestion

# 1. Simple panels for Faculty and Department 
admin.site.register(Faculty)
admin.site.register(Department)

# 2. Rich Structured panel for PastQuestion
class PastQuestionAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'department', 'semester', 'year', 'has_pdf', 'has_answer')
    list_filter = ('semester', 'year', 'department__faculty')
    search_fields = ('course_code', 'course_name', 'question_text')

    def has_pdf(self, obj):
        return bool(obj.pdf_file)
    has_pdf.boolean = True
    has_pdf.short_description = 'PDF'

    def has_answer(self, obj):
        return bool(obj.answer_text)
    has_answer.boolean = True
    has_answer.short_description = 'Answer Added'

admin.site.register(PastQuestion, PastQuestionAdmin)