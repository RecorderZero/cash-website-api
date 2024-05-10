from rest_framework import serializers
from .models import New, Classification, ProjectClassification, Project, Employee, Position, NewImage, ProjectImage, CarouselImage, User, Award, MemberCount

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class NewImageSerializer(serializers.ModelSerializer):
    
    # related_new = serializers.PrimaryKeyRelatedField(postid)

    class Meta:
        model = NewImage
        fields = '__all__'

class ProjectImageSerializer(serializers.ModelSerializer):
    
    # related_new = serializers.PrimaryKeyRelatedField(postid)

    class Meta:
        model = ProjectImage
        fields = '__all__'

class CarouselImageSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d")
    
    class Meta:
        model = CarouselImage
        fields = '__all__'

class NewSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d")

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
    startDate = serializers.DateField(format="%Y-%m-%d")
    endDate = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = Project
        fields = '__all__'
        read_only_field = ['id']
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_field = ['id']

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
        read_only_field = ['id']

class AwardSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d")
    
    class Meta:
        model = Award
        fields = '__all__'

class MemberCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberCount
        fields = '__all__'