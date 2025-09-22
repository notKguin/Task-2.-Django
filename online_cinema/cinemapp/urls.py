from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cookies/accept/', views.accept_cookies, name='accept_cookies'),
]