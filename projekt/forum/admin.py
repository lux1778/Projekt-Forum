from django.contrib import admin

from .models import Forum


# Register your models here.
@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'status']
    list_filter = ['status']
    search_fields = ['title','created_date']
    prepopulated_fields = {'slug' : ('title',)}
