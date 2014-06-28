from django.contrib import admin
from class_selector.models import Major, Class
# Register your models here.

#class MajorAdmin(admin.ModelAdmin):
    #list_display = ('major_name')
admin.site.register(Major)

class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'major', 'url')

admin.site.register(Class, ClassAdmin)
