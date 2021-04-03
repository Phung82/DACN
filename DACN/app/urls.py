from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gioithieu', views._about, name='abouttt'),
    path('chandoan', views._chandoan, name='chandoannn'),
    path('lienhe', views._lienhe, name='lienheee'),
]