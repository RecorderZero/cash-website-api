from .models import New, Classification, Project, ProjectClassification
from rest_framework import permissions, viewsets

from .serializers import NewSerializer, ClassificationSerializer, ProjectSerializer, ProjectClassificationSerializer
# from django.shortcuts import render

# Create your views here.
# 權限尚須調整 post,patch等需要權限
class NewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows new to be viewed or edited.
    """
    queryset = New.objects.all().order_by('id')
    serializer_class = NewSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
class ClassificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows classification to be viewed or edited.
    """
    queryset = Classification.objects.all().order_by('id')
    serializer_class = ClassificationSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
class ProjectClassificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows classification to be viewed or edited.
    """
    queryset = ProjectClassification.objects.all().order_by('id')
    serializer_class = ProjectClassificationSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows project to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer
    # permission_classes = [permissions.IsAuthenticated]