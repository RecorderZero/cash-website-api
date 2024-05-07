from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core import serializers
import json
from urllib.parse import unquote
# from django.contrib.auth.hashers import check_password

from .models import New, Classification, Project, ProjectClassification, Employee, Position, NewImage, ProjectImage, CarouselImage, User
from rest_framework import permissions, viewsets, status

from .serializers import NewSerializer, ClassificationSerializer, ProjectSerializer, ProjectClassificationSerializer, EmployeeSerializer, PositionSerializer, NewImageSerializer, ProjectImageSerializer, CarouselImageSerializer, UserSerializer
# from django.shortcuts import render

# Create your views here.
# 權限尚須調整 post,patch等需要權限

TRANSLATE_ADDR = 'http://127.0.0.1:8000'

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to be viewed or edited.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # 獲取用戶輸入的員工姓名
        employee_name = request.data.get('name')
        
        # 查找該員工是否已有帳號
        existing_user = User.objects.filter(name=employee_name).first()
        if existing_user:
            # 如果已經存在，返回錯誤訊息
            return Response({'error': '已經存在帳號'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 查找是否存在對應的員工
        employee = Employee.objects.filter(name=employee_name).first()
        
        if not employee:
            # 如果不存在，返回錯誤訊息
            return Response({'error': '資料尚未登錄'}, status=status.HTTP_400_BAD_REQUEST)

        # 如果存在，則創建新的用戶
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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

def get_project_images_detail(request, project_id):
    project_instance = get_object_or_404(Project, pk=project_id)
    project_images = project_instance.images.all().order_by('id')

    # 使用 projectImageSerializer 序列化 project_images
    serializer = ProjectImageSerializer(project_images, many=True)
    serialized_data = serializer.data
    
    # 遍历每个图像对象，修改其中的 URL 字段
    for image_data in serialized_data:
        image_data['image'] = TRANSLATE_ADDR + image_data['image']

    # 返回序列化后的数据给前端
    return JsonResponse(serialized_data, safe=False) 

def get_new_images_detail(request, new_id):
    new_instance = get_object_or_404(New, pk=new_id)
    new_images = new_instance.images.all().order_by('id')

    # 使用 NewImageSerializer 序列化 new_images
    serializer = NewImageSerializer(new_images, many=True)
    serialized_data = serializer.data
    
    # 遍历每个图像对象，修改其中的 URL 字段
    for image_data in serialized_data:
        image_data['image'] = TRANSLATE_ADDR + image_data['image']

    # 返回序列化后的数据给前端
    return JsonResponse(serialized_data, safe=False)    

def get_new_with_images(request, new_id):
    new_instance = get_object_or_404(New, pk=new_id)
    new_images = new_instance.images.all().order_by('id')
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

def get_project_with_images(request, project_id):
    project_instance = get_object_or_404(Project, pk=project_id)
    project_images = project_instance.images.all().order_by('id')
    image_urls = []
    # 將相關的projectImage數據轉換為JSON格式
    for project_image in project_images:
        image_url = TRANSLATE_ADDR + project_image.image.url
        image_urls.append(image_url)
        # image_urls = [new_image.image.url for new_image in new_images]
   
    # 使用 serializers 序列化 ManyToManyField
    employees_data = serializers.serialize('json', project_instance.employee.all())

    # 返回包含New和相關NewImage的JSON響應
    return JsonResponse({
        'title': project_instance.title,
        'content': project_instance.content,
        'image_urls': image_urls,
        'employee': employees_data,
        'location': project_instance.location,
        'startDate': project_instance.startDate,
        'endDate': project_instance.endDate
    })

def verify_user(request):
    user_account = request.GET.get('account')
    user = User.objects.filter(account=user_account).first()

    if not user:
        return JsonResponse({'error': '帳號不存在'}, status=400)
    
    user_password = request.GET.get('password')
    if user.password != user_password:
        return JsonResponse({'error': '密碼錯誤'}, status=400)

    return JsonResponse({'name': user.name.name, 'role': user.role}, status=200)

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
    queryset = CarouselImage.objects.all().order_by('order')
    serializer_class = CarouselImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            carouselOrder = request.data.get('order')
            carouselLocation = request.data.get('location')
            carouselDate = request.data.get('date')
            file = request.FILES.get('image')
            serializer.save(image=file, order=carouselOrder,
                            location=carouselLocation,
                            date=carouselDate,
                            displayornot=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_valid_carousel(request):
    # 獲取有效的carousel數據，按照order由小到大排序
    valid_carousel = CarouselImage.objects.filter(displayornot=True).order_by('order')

    # 根據?source參數返回不同的結果
    source = request.GET.get('source')

    if source == 'back':
        # 如果'?source=back'，回傳{'id': id, 'order': order}的物件陣列
        carousel_data = [{'id': carousel.id, 'order': carousel.order} for carousel in valid_carousel]
        return JsonResponse(carousel_data, safe=False)
    elif source == 'front':
        # 如果'?source=front'，回傳{'image_urls': image_urls}陣列
        carousel = [{'imageUrl': TRANSLATE_ADDR + carousel.image.url, 'location': carousel.location, 'date': carousel.date} for carousel in valid_carousel]
        return JsonResponse(carousel, safe=False)
    else:
        # 如果source參數不是'back'或'front'，返回錯誤響應
        return JsonResponse({'error': 'Invalid source parameter'})

# def get_valid_carousel(request):
#     valid_carousel = get_list_or_404(CarouselImage, displayornot=True)
#     image_urls = []
#     # 將有效的carousel數據轉換為JSON格式
#     for carousel in valid_carousel:
#         image_url = TRANSLATE_ADDR + carousel.image.url
#         image_urls.append(image_url)
#         # image_urls = [new_image.image.url for new_image in new_images]

#     # 返回carousel的JSON響應
#     return JsonResponse({
#         'image_urls': image_urls
#     }) 

class NewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows new to be viewed or edited.
    """
    # queryset = New.objects.all().order_by('-date', '-id')
    serializer_class = NewSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # 添加 basename 参数
    basename = 'new'

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category is None:
            queryset = New.objects.all().order_by('-date', '-id')

        else:
            category = unquote(category)
            queryset = New.objects.all().order_by('-date', '-id').filter(classification=category)
        
        return queryset

    def list(self, request, *args, **kwargs):
        # 从 URL 查询参数中获取要返回的 New 对象数量
        num_of_news = int(request.query_params.get('num', 0))

        # 如果返回全部，则直接使用父类的 list 方法处理查询结果
        if num_of_news == 0:
            return super().list(request, *args, **kwargs)

        # 否则根据日期和 ID 递减的顺序获取新闻，并根据 num_of_news 进行切片
        queryset = self.filter_queryset(self.get_queryset())[:num_of_news]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

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
    # queryset = Project.objects.all().order_by('-endDate', '-id')
    serializer_class = ProjectSerializer
    # permission_classes = [permissions.IsAuthenticated]
    basename = 'project'
    
    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category is None:
            queryset = Project.objects.all().order_by('-endDate', '-id')

        else:
            category = unquote(category)
            print(category)
            queryset = Project.objects.all().order_by('-endDate', '-id').filter(classification=category)
        
        return queryset
    
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Employee to be viewed or edited.
    """
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows position to be viewed or edited.
    """
    queryset = Position.objects.all().order_by('id')
    serializer_class = PositionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    