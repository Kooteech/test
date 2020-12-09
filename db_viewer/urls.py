from django.urls import path
from . import views

urlpatterns = [
    path('childdata/', views.get_childdata, name='get_childdata'),
]
