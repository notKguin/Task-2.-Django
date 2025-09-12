from django.urls import path

from .views import test_print

urlpatterns = [
    path('', test_print),
]
