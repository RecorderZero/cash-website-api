from rest_framework import serializers
from .models import New, Classification, ProjectClassification, Project, Member, Position

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'
        read_only_field = ['id']

class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'
        read_only_field = ['id']

class ProjectClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectClassification
        fields = '__all__'
        read_only_field = ['id']
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_field = ['id']
        
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        read_only_field = ['id']
        

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
        read_only_field = ['id']
