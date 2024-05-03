from django.db import models
from pygments.formatters.html import HtmlFormatter

# Create your models here.
class Position(models.Model):
    chinese_text = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return self.chinese_text

class Employee(models.Model):
    name = models.CharField(max_length=10, unique=True)
    position = models.ManyToManyField(Position, blank=True)
    education = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    office = models.CharField(max_length=10, null=True, blank=True)
    onboard_date = models.DateField()
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=40, unique=True)
    role = models.CharField(max_length=15, default='可讀')
    name = models.ForeignKey(Employee, to_field='name', on_delete=models.CASCADE)

    def __str__(self):
        return self.employeeId

class Classification(models.Model):
    chinese_text = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return self.chinese_text

class New(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    imageUrl = models.CharField(max_length=100, blank=True, null=True)
    classification = models.ForeignKey(Classification, to_field="chinese_text", on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # 刪除相關聯的 NewImage 實例以及其檔案
        for new_image in self.images.all():
            new_image.delete()
        super().delete(*args, **kwargs)

class NewImage(models.Model):
    image = models.ImageField(upload_to='news')
    related_new = models.ForeignKey(New, related_name='images', on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return self.image

    def delete(self, *args, **kwargs):
        # 刪除檔案
        self.image.delete()
        super().delete(*args, **kwargs)
    
class ProjectClassification(models.Model):
    chinese_text = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return self.chinese_text

class Project(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    imageUrl = models.CharField(max_length=100, blank=True, null=True)
    employee = models.ManyToManyField(Employee, blank=True)
    location = models.TextField(max_length=30, null=True)
    classification = models.ForeignKey(ProjectClassification, to_field="chinese_text", on_delete=models.CASCADE)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        # 刪除相關聯的 ProjectImage 實例以及其檔案
        for project_image in self.images.all():
            project_image.delete()
        super().delete(*args, **kwargs)

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects')
    related_project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return self.image

    def delete(self, *args, **kwargs):
        # 刪除檔案
        self.image.delete()
        super().delete(*args, **kwargs)

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousels')
    displayornot = models.BooleanField(default=True)
    order = models.IntegerField(null=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    # def __str__(self):
    #     return self.image