from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from core.models import Profile,Subject
from django.contrib.auth import authenticate, login

def register_student(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        reg_no = request.POST['reg_no']

        user = User.objects.create_user(
            username=username,
            password=password
        )

        Profile.objects.create(
            user=user,
            reg_no=reg_no,
            role='student'
        )

        return redirect('login')

    return render(request, 'accounts/register_student.html')
def register_teacher(request):

    subjects = Subject.objects.all()

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        reg_no = request.POST['reg_no']
        subject_id = request.POST.get('subject')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        subject = Subject.objects.get(id=subject_id)

        Profile.objects.create(
            user=user,
            reg_no=reg_no,
            role='teacher',
            subject=subject
        )

        return redirect('login')

    return render(request, 'accounts/register_teacher.html', {
        'subjects': subjects
    })



def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            role = user.profile.role

            if role == "teacher":
                return redirect('teacher_dashboard')
            else:
                return redirect('student_dashboard')

    return render(request, 'accounts/login.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')