from django.contrib import admin
from .models import student_db

# importing the models into django admin
class StudentAdmin(admin.ModelAdmin):
  list_display = ("name", "age", "gender", "student_Id")

admin.site.register(student_db, StudentAdmin)