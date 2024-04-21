from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from .models import New, Classification, Project, ProjectClassification, Member, Position, Snippet, Test, NewImage
from rest_framework import permissions, viewsets, status

from .form import UploadForm

from .serializers import NewSerializer, ClassificationSerializer, ProjectSerializer, ProjectClassificationSerializer, MemberSerializer, PositionSerializer, SnippetSerializer, TestSerializer, NewImageSerializer
# from django.shortcuts import render

# Create your views here.
# 權限尚須調整 post,patch等需要權限

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

# def upload(request):
#     if request.FILES:
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()

#     return JsonResponse({'success': True})

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

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