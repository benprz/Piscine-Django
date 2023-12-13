from django.urls import path
from d06.globals import init

urlpatterns = [
    path('init', init, name='init'),
]