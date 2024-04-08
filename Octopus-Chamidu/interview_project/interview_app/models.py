# interview_app/models.py

from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)

class Class(models.Model):
    name = models.CharField(max_length=255)

class AssessmentArea(models.Model):
    name = models.CharField(max_length=255)

class Student(models.Model):
    fullname = models.CharField(max_length=255)

class Answers(models.Model):
    answer = models.CharField(max_length=1)

class Summary(models.Model):
    school_id = models.IntegerField()
    sydney_participants = models.IntegerField()
    sydney_percentile = models.IntegerField()
    assessment_area_id = models.IntegerField()
    award_id = models.IntegerField()
    class_id = models.IntegerField()
    correct_answer_percentage_per_class = models.FloatField()
    correct_answer = models.CharField(max_length=1)
    student_id = models.IntegerField()
    participant = models.IntegerField()
    student_score = models.FloatField()
    subject_id = models.IntegerField()
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=255)
    answer_id = models.IntegerField()
    correct_answer_id = models.IntegerField()
