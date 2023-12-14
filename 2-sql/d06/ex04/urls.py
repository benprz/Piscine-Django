from django.urls import path
from d06.globals import init

from . import views

urlpatterns = [
    path('init', init, name='init'),
    path('populate', views.populate, name='populate'),
    path('display', views.display, name='display'),
    path('remove', views.remove, name='remove'),
]