from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Student_Database)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('Student_Information','Date')
    search_fields = ['Student_Information']
    list_filter = ('Student_Information',)

admin.site.register(Records,RecordAdmin)
