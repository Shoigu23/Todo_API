from django.contrib import admin
from main.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)

admin.site.register(Student, StudentAdmin)
