from django.db import models

# Create your models here.

class Major(models.Model):
    major_name = models.CharField(max_length = 50, unique = True)
    
    def __str__(self):
        return self.major_name

class Class (models.Model):
    major = models.ForeignKey(Major)
    class_name = models.CharField(max_length = 128)
    url = models.URLField()
    next_sem = models.CharField(max_length = 20)
    frequency = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.class_name
    class Meta:
        verbose_name_plural = "Classes"