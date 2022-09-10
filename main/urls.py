from django.urls import path
from .views import *

urlpatterns = [
    path('', about, name='about'),
    path('projects/', projects_page, name='projects'),
    path('contacts/', contacts, name='contacts'),
    path('project/<pk>', project_info, name='project'),
    path('visual/<pk>', visual_info, name='visual')
]
