from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('impressum/', views.impressum, name='impressum' ),
    path('reg/', views.reg, name='register' ),


]