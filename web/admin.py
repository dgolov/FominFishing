from django.contrib import admin
from .models import Service, Photo, Review, Request


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
