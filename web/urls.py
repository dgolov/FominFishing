from django.urls import path

from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('about', views.AboutView.as_view(), name='about'),
    path('boat', views.BoatView.as_view(), name='boat'),
    path('service', views.ServiceView.as_view(), name='service'),
    path('gallery', views.GalleryView.as_view(), name='gallery'),
    path('video', views.VideoView.as_view(), name='video'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('advertising', views.AdvertisingView.as_view(), name='advertising'),
    path('calendar', views.CalendarView.as_view(), name='calendar'),
    path('reviews', views.ReviewView.as_view(), name='reviews'),
]
