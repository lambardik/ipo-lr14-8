from django.urls import path
from .views import index, tema,me

urlpatterns = [
    path('me/', me, name='me'), 
    path('tema/', tema, name='tema'), 
    path('', index, name='index'), 
    
]

