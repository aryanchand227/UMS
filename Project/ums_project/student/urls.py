from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='student_dashboard'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('timetable/', views.timetable_view, name='student_timetable'),
    path('messages/', views.inbox, name='student_messages'),
    path('cgpa/', views.view_cgpa, name='student_cgpa'),
    path('courses/', views.view_courses, name='student_courses'),
]