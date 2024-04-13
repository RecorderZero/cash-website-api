from django.contrib import admin
from .models import New, Classification, Project, ProjectClassification, Member, Position

# Register your models here.
admin.site.register(New)
admin.site.register(Classification)
admin.site.register(ProjectClassification)
admin.site.register(Project)
admin.site.register(Member)
admin.site.register(Position)