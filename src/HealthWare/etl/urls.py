from django.urls import path
from . import views

app_name = 'etl'

urlpatterns = [
    path('', views.login, name='login'),
    ]
