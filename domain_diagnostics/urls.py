from django.urls import path
from domain_speed import views

urlpatterns = [
    path('', views.speed_html, name='speed_html'),
    path('speed.html', views.speed_html, name='speed_html'),
    path('speed.json', views.speed_json, name='speed_json'),
]
