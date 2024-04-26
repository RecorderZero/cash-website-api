from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import New, Classification, Project, ProjectClassification, Member, Position, Snippet, Test, NewImage, ProjectImage, CarouselImage
from rest_framework import permissions, viewsets, status

from .serializers import NewSerializer, ClassificationSerializer, ProjectSerializer, ProjectClassificationSerializer, MemberSerializer, PositionSerializer, SnippetSerializer, TestSerializer, NewImageSerializer, ProjectImageSerializer, CarouselImageSerializer
# from django.shortcuts import render

# Create your views here.
# 權限尚須調整 post,patch等需要權限

TRANSLATE_ADDR = 'http://127.0.0.1:8000'

class NewImageViewSet(viewsets.ModelViewSet):
    queryset = NewImage.objects.all()
    serializer_class = NewImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            for file in request.FILES.getlist('image'):
                serializer.save(image=file)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def perform_create(self, serializer):
    #     serializer.save(post=post.id) 需要自動儲存newid

def get_new_with_images(request, new_id):
    new_instance = get_object_or_404(New, pk=new_id)
    new_images = new_instance.images.all()
    image_urls = []
    # 將相關的NewImage數據轉換為JSON格式
    for new_image in new_images:
        image_url = TRANSLATE_ADDR + new_image.image.url
        image_urls.append(image_url)
        # image_urls = [new_image.image.url for new_image in new_images]

    # 返回包含New和相關NewImage的JSON響應
    return JsonResponse({
        'title': new_instance.title,
        'content': new_instance.content,
        'image_urls': image_urls
    })

class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            for file in request.FILES.getlist('image'):
                serializer.save(image=file)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class CarouselImageViewSet(viewsets.ModelViewSet):
    queryset = CarouselImage.objects.all()
    serializer_class = CarouselImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        request.data['displayornot'] = True
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            for file in request.FILES.getlist('image'):
                serializer.save(image=file)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_valid_carousel(request):
    valid_carousel = get_list_or_404(CarouselImage, displayornot=True)
    image_urls = []
    # 將有效的carousel數據轉換為JSON格式
    for carousel in valid_carousel:
        image_url = TRANSLATE_ADDR + carousel.image.url
        image_urls.append(image_url)
        # image_urls = [new_image.image.url for new_image in new_images]

    # 返回carousel的JSON響應
    return JsonResponse({
        'image_urls': image_urls
    }) 

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class NewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows new to be viewed or edited.
    """
    queryset = New.objects.all().order_by('-date')
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
    queryset = Project.objects.all().order_by('-date')
    serializer_class = ProjectSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows member to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('id')
    serializer_class = MemberSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows position to be viewed or edited.
    """
    queryset = Position.objects.all().order_by('id')
    serializer_class = PositionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)