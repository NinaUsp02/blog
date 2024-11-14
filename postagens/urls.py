from django.urls import path

from . import views

app_name = 'postagens'
urlpatterns = [
    path("", views.list_postagens, name="index"),
    path('search/', views.search_postagens, name='search'),
    path('create/', views.create_postagem, name='create'),
    path('<int:postagem_id>/', views.detail_postagem, name='detail'),
    path('update/<int:postagem_id>/', views.update_postagem, name='update'),
    path('delete/<int:postagem_id>/', views.delete_postagem, name='delete'),

 ]