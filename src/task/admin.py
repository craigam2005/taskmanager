from django.contrib import admin
from .models import Task
admin.autodiscover()

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    
    '''fieldsets = [
        ('title',       {'fields': ['title']}),
        ('priority',    {'fields': ['priority']}),
        ('Guts Ticket', {'fields': ['guts_ticket']}),
        ('Created',    {'fields': ['created_date']}),
        ('Due Date',    {'fields': ['due_date']}),
        ('Done',        {'fields': ['done']}),
    
    ]'''
    actions_on_top = True
    actions = ['mark_done']
    
    list_display = ('title','priority','guts_ticket','due_date','created_date','done')    

    date_hierarchy = 'due_date'
    ordering = ['priority', date_hierarchy]
    list_filter = ['priority', date_hierarchy]
    
    
    def mark_done(self, request, queryset):
        rows_updated = queryset.update(done='d')
        if rows_updated == 1:
            message_bit = '1 task was'
        else:
            message_bit = '%s stories were '% rows_updated
        self.message_user(request, '%s successfuly marked as done.'% message_bit)
   
admin.site.register(Task,TaskAdmin)