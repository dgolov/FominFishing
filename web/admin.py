from django.contrib import admin
from .models import Category, Service, Photo, Review, Request, Video, Calendar


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Отображение услуг в админке
    """
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """ Отображение услуг в админке
    """
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Отображение услуг в админке
    """
    list_display = ['id', 'path']
    list_display_links = ['id', 'path']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Отображение услуг в админке
    """
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    """ Отображение услуг в админке
    """
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """ Отображение услуг в админке
    """
    list_display = ['id', 'title', 'added_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    """ Отображение дат рыбалок
    """
    list_display = ['id', 'title', 'start_date', 'end_date']
    list_display_links = ['title']
    search_fields = ['title']
