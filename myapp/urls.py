from django.urls import path
from .views import index, inde,ind

urlpatterns = [
    path('inde/', inde, name='inde'), 
    path('ind', ind, name='ind'), 
    path('', index, name='index'), 
]

