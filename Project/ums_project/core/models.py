from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    name = models.CharField(max_length=100)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Sem {self.semester})"


# 🔹 Profile
class Profile(models.Model):

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=10)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # NEW → teacher subject
    subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username


# 🔹 Attendance (UPDATED)
class Attendance(models.Model):

    student = models.ForeignKey(User, on_delete=models.CASCADE)

    subject = models.ForeignKey(
    Subject,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    date = models.DateField()

    present = models.BooleanField(default=False)

class SubjectScore(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_scores'
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='teacher_scores'
    )

    points = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.points}"
    



    
# 🔹 CGPA
class CGPA(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    cgpa = models.FloatField()


# 🔹 Course (unchanged)
class Course(models.Model):
    name = models.CharField(max_length=100)
    semester = models.IntegerField()


# 🔹 Timetable
class Timetable(models.Model):
    day = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)


# 🔹 Message
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)