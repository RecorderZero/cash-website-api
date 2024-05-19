from rest_framework import serializers
from .models import New, Classification, ProjectClassification, Project, Employee, Position, NewImage, ProjectImage, CarouselImage, User, HistoryAward, MemberCount, ChosenAward

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

class HistoryAwardSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d")
    
    class Meta:
        model = HistoryAward
        fields = '__all__'

class MemberCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberCount
        fields = '__all__'

class ChosenAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenAward
        fields = '__all__'

    def update(self, instance, validated_data):
        # 檢查是否有新的 image
        new_image = validated_data.get('image', None)

        if new_image:
            # 如果有新的 image，刪除舊的 image
            if instance.image:
                instance.image.delete()
            instance.image = new_image

        # 更新 title 和 link
        instance.title = validated_data.get('title', instance.title)
        instance.link = validated_data.get('link', instance.link)

        # 保存實例
        instance.save()
        return instance
