from django.urls import path

from .views import MainView, AboutView, BoatView, ServiceView, GalleryView, ContactView, VideoView, AdvertisingView, CalendarView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('about', AboutView.as_view(), name='about'),
    path('boat', BoatView.as_view(), name='boat'),
    path('service', ServiceView.as_view(), name='service'),
    path('gallery', GalleryView.as_view(), name='gallery'),
    path('video', VideoView.as_view(), name='video'),
    path('contact', ContactView.as_view(), name='contact'),
    path('advertising', AdvertisingView.as_view(), name='advertising'),
    path('calendar', CalendarView.as_view(), name='calendar'),
]
