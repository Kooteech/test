from django.urls import path, re_path
from . import views

urlpatterns = [
    path('childdata/', views.get_childdata, name='get_childdata'),
    path(r'childdata/moreinfo/', views.get_more_info)

]
