from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='teacher_dashboard'),
    path('attendance/', views.mark_attendance, name='mark_attendance'),
    path('timetable/', views.add_timetable, name='add_timetable'),
    path('messages/', views.send_message, name='send_message'),
    path('points/', views.upload_points, name='upload_points'),
]