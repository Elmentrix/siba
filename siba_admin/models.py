from django.db import models
import json

# creating admin user function tables
class Courses(models.Model):
    course_Id = models.CharField(max_length=100, primary_key=True)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

# table for elective subjects
class Subjects(models.Model)        :
    subject = models.CharField(max_length=100)
    course_alloc = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.subject


# table for assignments
class Assignments(models.Model):
    student = models.ForeignKey('siba_student.student_db', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.student.name


# table for time table
class TimeTable(models.Model):
    # data = models.CharField(max_length=100)
    # stored_time = models.DateTimeField(auto_now_add=True)

    

    timetable_data = models.TextField(null=True)
    TimeGenerated = models.DateTimeField(auto_now_add=True)

    def save_timetable_data(self, data):
        self.timetable_data = json.dumps(data)
        self.save()

    def get_timetable_data(self):
        return json.loads(self.timetable_data)

    def __str__(self):
        return f'Timetable: {self.TimeGenerated}'

