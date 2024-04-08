# interview_app/admin.py

from django.contrib import admin
from .models import School, Class, AssessmentArea, Student, Answers, Summary

# Register your models here

admin.site.register(School)
admin.site.register(Class)
admin.site.register(AssessmentArea)
admin.site.register(Student)
admin.site.register(Answers)
admin.site.register(Summary)
