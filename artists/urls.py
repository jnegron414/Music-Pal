from django.urls import path

from artists import views

app_name = 'artists'
urlpatterns = [
    path('', views.list, name='list'),
    path('<str:artist_slug>/', views.detail, name='detail'),
]