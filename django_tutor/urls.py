"""
URL configuration for django_tutor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from cash_website import views

# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

router = routers.DefaultRouter()
router.register(r'new', views.NewViewSet)
router.register(r'classification', views.ClassificationViewSet)
router.register(r'projectclassification', views.ProjectClassificationViewSet)
router.register(r'project', views.ProjectViewSet)
router.register(r'member', views.MemberViewSet)
router.register(r'position', views.PositionViewSet)
router.register(r'test', views.TestViewSet)
router.register(r'newimage', views.NewImageViewSet)
router.register(r'projectimage', views.ProjectImageViewSet)
router.register(r'carouselimage', views.CarouselImageViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('cash_website.urls')),
    path('get_new_with_images/<int:new_id>/', views.get_new_with_images),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
