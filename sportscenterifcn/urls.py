from django.urls import path

from sportscenterifcn import views

app_name = 'sportscenterifcn'

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
