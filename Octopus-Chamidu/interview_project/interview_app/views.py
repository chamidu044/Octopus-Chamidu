from django.shortcuts import render
from .models import School, Class, AssessmentArea, Student, Answers, Summary

def view_data(request):
    # Retrieve data from models
    schools = School.objects.all()
    classes = Class.objects.all()
    assessment_areas = AssessmentArea.objects.all()
    students = Student.objects.all()
    answers = Answers.objects.all()
    summaries = Summary.objects.all()

    # Pass data to template context
    context = {
        'schools': schools,
        'classes': classes,
        'assessment_areas': assessment_areas,
        'students': students,
        'answers': answers,
        'summaries': summaries,
    }

    # Render custom template with data
    return render(request, 'interview_app/view_data.html', context)
