from django.contrib import admin
from .models import Event
from .models import Task




class Task(admin.TabularInline):
    model = Task
    extra = 1
    
class EventAdmin(admin.ModelAdmin):
    fieldsets = []
    inlines = [Task]
    list_filter = ['date']
   
admin.site.register(Event,EventAdmin)


