from django.urls import path
from . import views

app_name = 'apps.about'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('probar/', views.probar, name='probar'),
]