from django.contrib import admin
from .models import Courses, Assignments, Subjects, TimeTable

# importing the models into django admin
class Courses_in(admin.ModelAdmin):
    list_display = [field.name for field in Courses._meta.fields]

admin.site.register(Courses, Courses_in)
admin.site.register(Subjects)
admin.site.register(Assignments)
admin.site.register(TimeTable)