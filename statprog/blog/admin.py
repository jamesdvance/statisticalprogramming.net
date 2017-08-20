from django.contrib import admin
from blog.models import Category, Blog, Topic
# Register your models here.

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Topic)
