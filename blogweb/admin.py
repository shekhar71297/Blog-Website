from django.contrib import admin
from . models import Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('author',)}
    list_display=['author','title']

# Register your models here.
admin.site.register(Blog,BlogAdmin)
