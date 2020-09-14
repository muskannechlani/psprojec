from .views import print,showhtml
from django.urls import path

urlpatterns = [
    path('abc', print, name='home1'),
    path('', showhtml)
]
