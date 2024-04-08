# load_data.py

import os
import csv
from django.db import transaction
from interview_app.models import School, Class, AssessmentArea, Student, Answers, Summary

@transaction.atomic
def load_data():
    csv_directory = '/Users/chamiduhimantha/Desktop/octatest/Ganison_dataset/Ganison_dataset_1.csv'

    for filename in os.listdir(csv_directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(csv_directory, filename)
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        # Create School if not exists
                        school, _ = School.objects.get_or_create(name=row['school_name'])

                        # Create Class if not exists
                        class_obj, _ = Class.objects.get_or_create(name=row['Class'])

                        # Create AssessmentArea if not exists
                        area, _ = AssessmentArea.objects.get_or_create(name=row['Assessment Areas'])

                        # Create Student if not exists
                        student_name = f"{row['First Name']} {row['Last Name']}"
                        student, _ = Student.objects.get_or_create(fullname=student_name)

                        # Create Answers if not exists
                        answer, _ = Answers.objects.get_or_create(answer=row['Answers'])

                        # Create Summary entry
                        Summary.objects.create(
                            school_id=school.id,
                            sydney_participants=row['sydney_participants'],
                            sydney_percentile=row['sydney_percentile'],
                            assessment_area_id=area.id,
                            award_id=row['award'],  # Assuming award_id corresponds to some value
                            class_id=class_obj.id,
                            correct_answer_percentage_per_class=row['correct_answer_percentage_per_class'],
                            correct_answer=row['Correct Answers'],
                            student_id=student.id,
                            participant=row['participant'],
                            student_score=row['student_score'],
                            subject_id=row['Subject'],  # Assuming subject_id corresponds to some value
                            category_id=row['Category'],  # Assuming category_id corresponds to some value
                            year_level_name=row['Year Level'],  # Assuming year_level_name is a string
                            answer_id=answer.id,
                            correct_answer_id=row['Correct Answers']  # Assuming correct_answer_id corresponds to some value
                        )
                        print(f"Successfully processed row for file: {filename}")
                    except Exception as e:
                        print(f"Error processing row for file {filename}: {e}")

if __name__ == "__main__":
    load_data()
