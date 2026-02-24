

# Register your models here.
from django.contrib import admin
from .models import Course,SubjectScore, Profile, Attendance, CGPA, Timetable, Message,Subject

admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(Attendance)
admin.site.register(CGPA)
admin.site.register(Timetable)
admin.site.register(Message)
admin.site.register(Subject)
admin.site.register(SubjectScore)