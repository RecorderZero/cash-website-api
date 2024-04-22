from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0],item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class Position(models.Model):
    chinese_text = models.CharField(max_length=15)
    english_text = models.CharField(max_length=30)
    
    def __str__(self):
        return self.chinese_text

class Member(models.Model):
    name = models.CharField(max_length=10)
    position = models.ManyToManyField(Position)
    education = models.TextField(null=True)
    experience = models.TextField(null=True)
    office = models.CharField(max_length=10)
    onboard_date = models.DateField()
    
    def __str__(self):
        return self.name
    
class Classification(models.Model):
    chinese_text = models.CharField(max_length=15)
    english_text = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.chinese_text

class New(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    imageUrl = models.JSONField("imageUrl", default=dict, blank=True, null=True)
    classification = models.ForeignKey(Classification, to_field="english_text", on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return self.title
    
class ProjectClassification(models.Model):
    chinese_text = models.CharField(max_length=15)
    english_text = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.chinese_text

class Project(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    imageUrl = models.JSONField("imageUrl", default=dict, blank=True, null=True)
    member = models.ManyToManyField(Member)
    location = models.TextField(max_length=30, null=True)
    classification = models.ForeignKey(ProjectClassification, to_field="english_text", on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return self.title
    
class NewImage(models.Model):
    image = models.ImageField(upload_to='news')
    related_new = models.ForeignKey(New, related_name='images', on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return self.image

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects')
    related_project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return self.image

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousels')
    displayornot = models.BooleanField(default=True)
    
    # def __str__(self):
    #     return self.image

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['created']

class Test(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()

    def __str__(self):
        return self.title
    
