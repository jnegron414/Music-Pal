from django.urls import path

from homepage import views

app_name = 'artists'
urlpatterns = [
    path('', views.list, name='list'),
    path('<str:artist_slug>/', views.detail, name='detail'),
]