from django.urls import path
from .views import *

app_name= 'app'
urlpatterns = [
    path('run1', run1, name="run1"),
    path('run2', run2, name="run2"),
    path('custom', custom, name="custom"),
]