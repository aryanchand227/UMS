from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Attendance,SubjectScore, Timetable, Message, Subject
from django.db.models import Avg

@login_required(login_url='/')
def dashboard(request):
    return render(request, 'student/dashboard.html')


from django.db.models import Count, Q

@login_required(login_url='/')
def attendance_view(request):

    records = Attendance.objects.filter(student=request.user)

    # Aggregate
    total = records.count()
    present = records.filter(present=True).count()
    percent = (present / total * 100) if total else 0

    # Subject-wise
    subjects = records.values('subject__name').annotate(
        total=Count('id'),
        present=Count('id', filter=Q(present=True))
    )

    return render(request, 'student/attendance.html', {
        'records': records,
        'percent': percent,
        'present': present,
        'total': total,
        'subjects': subjects
    })

@login_required(login_url='/')
def timetable_view(request):
    table = Timetable.objects.all()
    return render(request, 'student/timetable.html', {'table': table})


@login_required(login_url='/')
def inbox(request):
    msgs = Message.objects.filter(receiver=request.user).order_by('-timestamp')    
    return render(request, 'student/messages.html', {'msgs': msgs})




@login_required(login_url='/')
def view_cgpa(request):

    scores = SubjectScore.objects.filter(
        student=request.user
    )

    avg = scores.aggregate(Avg('points'))['points__avg']

    return render(request, 'student/cgpa.html', {
        'cgpa': round(avg, 2) if avg else None
    })

@login_required(login_url='/')
def view_courses(request):

    current_sem = 6  # You can later make dynamic

    subjects = Subject.objects.filter(semester=current_sem)

    return render(request, 'student/courses.html', {
        'subjects': subjects,
        'sem': current_sem
    })