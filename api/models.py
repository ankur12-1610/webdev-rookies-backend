from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Classroom(models.Model):
#a class is created by teacher(user)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=255)
    classroom_color = models.CharField(max_length=255, default="blue")
    classroom_link = models.CharField(max_length=255, default="None")
    # #color choices code
    # BLUE=0
    # RED=1
    # VIOLET=2
    # GREEN=3
    
    # PROFILE_PICTURE_CHOICES = (
    #     (str(BLUE), 'Blue-theme'),
    #     (str(RED), 'Red-theme'),
    #     (str(VIOLET), 'Violet-theme'),
    #     (str(GREEN), 'Green-theme'),
    # )

    def __str__(self):
        return self.title
 
class Student(models.Model):
#a single class has enrolled students
    students = models.ManyToManyField(User, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.classroom.title

class Assignment(models.Model):
#assignment is created by teacher(user)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=255)
    deadline = models.DateTimeField(default=datetime.now, blank=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null = True)
    score = models.CharField(max_length=255, default="ungraded")
    # Score choices codes:
    # UNGRADED = 0
    # POOR = 1
    # BELOW_AVERAGE = 2
    # AVERAGE = 3
    # GOOD = 4
    # EXCELLENT = 5

    # SCORE_CHOICES = (
    #     (str(UNGRADED), 'Ungraded'),
    #     (str(POOR), ('1 - Very Poor')),
    #     (str(BELOW_AVERAGE), ('2 - Below Average')),
    #     (str(AVERAGE), ('3 - Average')),
    #     (str(GOOD), ('4 - Good')),
    #     (str(EXCELLENT), ('5 - Excellent'))
    # )

    # score = models.BooleanField(choices=SCORE_CHOICES, default=UNGRADED)

    def __str__(self):
        return self.title
    

class AssignmentStatus(models.Model):
#assignment status is defined to a single student
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null = True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    
    BOOL_CHOICES = ((True, 'Completed'), (False, 'Incomplete'))

    status = models.BooleanField(choices=BOOL_CHOICES, default=False)

    def __str__(self):
        return self.student.username

#for images

# class Image(models.Model):
#     name = models.CharField(max_length=255)
#     # image = models.ImageField(max_length=800, null=True, use_url='images/')
#     image = models.CharFieField(max_length=800, null=True)
#     def __str__(self):
#         return self.name