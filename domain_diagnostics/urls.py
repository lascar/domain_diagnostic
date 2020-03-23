from django.urls import path
from domain_speed import views

urlpatterns = [
    path('', views.speed, name='speed')
]
