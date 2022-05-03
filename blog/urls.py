from django.urls import path

from .views import BlogView


urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    # path('<str:slug>/', BlogView.as_view(), name='blog'),
]
