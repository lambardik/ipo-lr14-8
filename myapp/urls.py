from django.urls import path
from .views import index, dggfd

urlpatterns = [
    path('', index, name='index'),
     path('dggfd', dggfd, name='dggfd'),
]
