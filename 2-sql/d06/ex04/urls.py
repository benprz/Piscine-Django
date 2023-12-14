from django.urls import path
from d06.globals import init

from . import views
from ex02 import views as ex02_views

urlpatterns = [
    path('init', init, name='init'),
    path('populate', ex02_views.populate, name='populate'),
    path('display', ex02_views.display, name='display'),
    path('remove', views.remove, name='remove'),
]