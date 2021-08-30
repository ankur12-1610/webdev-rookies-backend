from django.db.models import query
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.generics import *
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.http import Http404  


class ClassroomViewSet(viewsets.ModelViewSet):
    """
        Classroom_colors:
        BLUE=0
        RED=1
        VIOLET=2
        GREEN=3
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ClassroomSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return Classroom.objects.all()
    
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()

class AssignmentViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AssignmentSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)
    

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Assignment.objects.all()

class AssignmentStatusViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AssignmentStatusSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return AssignmentStatus.objects.all()

# class ImageViewSet(viewsets.ModelViewSet):
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = ImageSerializer

#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)


#     def get_queryset(self):
#         return Image.objects.all()