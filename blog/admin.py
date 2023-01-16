from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import Subject, Teacher
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('no','name','intro','is_hot')
    search_fields = ('name',)
    ordering = ('no',)

class TeachermodelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'sex', 'birth', 'good_count', 'bad_count', 'subject')
    search_fields = ('name',)
    ordering = ('no',)

admin.site.register(Subject,SubjectModelAdmin)
admin.site.register(Teacher,TeachermodelAdmin)