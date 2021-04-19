from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('index/',index),
    path('about/',about),
    path('base/',base),
    path('contact/',Contact),
    path('propertygrid/',propertyGgrid),
    path('propertysingle/',propertySingle),
    path('bloggrid/',blogGrid),
    path('blogsingle/',blogSingle),
    path('agentsgrid/',agentsGrid),
    path('agentsingle/',agentSingle),
]