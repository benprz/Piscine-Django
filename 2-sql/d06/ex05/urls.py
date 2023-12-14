from django.urls import path
from d06.globals import init

from . import views
from ex03 import views as ex03_views

urlpatterns = [
    path('populate', ex03_views.populate, name='populate'),
    path('display', ex03_views.display, name='display'),
    path('remove', views.remove, name='remove'),
]