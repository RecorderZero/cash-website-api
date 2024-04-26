from django.contrib import admin
from .models import New, Classification, Project, ProjectClassification, Employee, Position, NewImage, ProjectImage, CarouselImage

# Register your models here.
admin.site.register(New)
admin.site.register(Classification)
admin.site.register(ProjectClassification)
admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(NewImage)
admin.site.register(ProjectImage)
admin.site.register(CarouselImage)