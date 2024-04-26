from rest_framework import serializers
from .models import New, Classification, ProjectClassification, Project, Member, Position, Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Test, NewImage, ProjectImage, CarouselImage
from django.contrib.auth.models import User

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
    class Meta:
        model = CarouselImage
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
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

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']
        owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance