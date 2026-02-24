from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.utils import teacher_required
from core.models import Attendance, Timetable, Message, SubjectScore
from django.contrib import messages
from datetime import date


@login_required(login_url='/')
@teacher_required
def dashboard(request):
    return render(request, 'teacher/dashboard.html')




@login_required(login_url='/')
@teacher_required
def mark_attendance(request):

    students = User.objects.filter(profile__role='student')

    subject = request.user.profile.subject

    if request.method == "POST":

        for student in students:

            present = request.POST.get(str(student.id)) == "on"

            Attendance.objects.create(
                student=student,
                subject=subject,
                present=present,
                date=date.today()
            )

        messages.success(request, "Attendance marked successfully")
        return redirect('mark_attendance')

    return render(request, 'teacher/mark_attendance.html', {
        'students': students
    })

@login_required(login_url='/')
@teacher_required
def add_timetable(request):
    if request.method == "POST":
        Timetable.objects.create(
            day=request.POST.get('day', ''),
            subject=request.POST.get('subject', ''),
            time=request.POST.get('time', ''),
            teacher=request.user
        )
        messages.success(request, "Timetable entry added")
        return redirect('add_timetable')
    table = Timetable.objects.filter(teacher=request.user)

    return render(request, 'teacher/timetable.html', {
    'table': table
    })    


@login_required(login_url='/')
@teacher_required
def send_message(request):
    students = User.objects.filter(profile__role='student')

    if request.method == "POST":
        student_id = request.POST.get('student')
        content = request.POST.get('content', '').strip()

        if student_id:
            try:
                student = User.objects.get(id=student_id)
                Message.objects.create(sender=request.user, receiver=student, content=content)
            except User.DoesNotExist:
                messages.error(request, "Selected student not found.")
        else:
            for student in students:
                Message.objects.create(sender=request.user, receiver=student, content=content)

        messages.success(request, "Message sent successfully")
        return redirect('send_message')

    return render(request, 'teacher/messages.html', {
        'students': students
    })



@login_required(login_url='/')
@teacher_required
def upload_points(request):

    students = User.objects.filter(profile__role='student')
    subject = request.user.profile.subject

    if request.method == "POST":

        for student in students:

            points = request.POST.get(str(student.id))

            if points:
                SubjectScore.objects.update_or_create(
                    student=student,
                    subject=subject,
                    teacher=request.user,
                    defaults={'points': points}
                )

        messages.success(request, "Points uploaded successfully")
        return redirect('upload_points')

    return render(request, 'teacher/points.html', {
        'students': students,
        'subject': subject
    })