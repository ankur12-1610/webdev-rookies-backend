from rest_framework import  serializers
from .models import *
from django.contrib.auth.models import User
from authentication.serializers import *


class ClassroomSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source = 'teacher.username', required = False, read_only = True)
    teacher_id = serializers.IntegerField(source = 'teacher.id', required = False, read_only = True)

    def save(self, **kwargs):
        data = self.validated_data
        user = self.context['request'].user
        title = data['title']
        classroom = Classroom.objects.create(teacher=user, title=title)
        classroom.save()

    class Meta:
        model = Classroom
        fields = ('id', 'title', 'teacher', 'teacher_id', 'classroom_color','classroom_link')

class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.CharField(source = 'classroom.title', required = False, read_only = True)
    classroom_id = serializers.IntegerField(source = 'classroom.id', required = False, read_only = True)
    student_id = serializers.IntegerField(source = 'id', required = False, read_only = True)
    class Meta:
        model = Student
        fields = ('student_id','classroom','classroom_id','students',)

class AssignmentSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source = 'teacher.username', required = False, read_only = True)
    assignment_id = serializers.IntegerField(source = 'assignment.id', required = False, read_only = True)

    def save(self, **kwargs):
        data = self.validated_data
        user = self.context['request'].user
        title = data['title']
        assignment = Assignment.objects.create(teacher=user, title=title)
        assignment.save()

    classroom = serializers.CharField(source = 'classroom.title', required = False, read_only = True)
    classroom_id = serializers.IntegerField(source = 'classroom.id', required = False, read_only = True)
    class Meta:
        model = Assignment
        fields = ('assignment_id','title','teacher','classroom','classroom_id','deadline','score',)

class AssignmentStatusSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source = 'student.username', required = False, read_only = True)
    student_id = serializers.IntegerField(source = 'student.id', required = False, read_only = True)
    assignment = serializers.CharField(source = 'assignment.title', required = False, read_only = True)
    assignment_id = serializers.IntegerField(source = 'assignment.id', required = False, read_only = True)
    class Meta:
        model = AssignmentStatus
        fields = ('assignment_id','assignment','student','student_id','status',)


# class ImageSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(
#         sizes = {
#             'small': (300, 300),
#             'medium': (500, 500),
#             'large': (700, 700),
#         },required=True,
#     )

#     class Meta:
#         model = Image
#         fields = ['pk', 'name', 'image']
