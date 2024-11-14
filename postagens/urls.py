from django.urls import path

from . import views

app_name = 'postagens'
urlpatterns = [
    path('', views.PostagemListView.as_view(), name='index'),
    path('search/', views.PostagemSearchView.as_view(), name='search'),
    path('create/', views.PostagemCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostagemDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.PostagemUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostagemDeleteView.as_view(), name='delete'),
"""     path('search/', views.search_postagens, name='search'),
    path('create/', views.create_postagem, name='create'),
    path('<int:postagem_id>/', views.detail_postagem, name='detail'),
    path('update/<int:postagem_id>/', views.update_postagem, name='update'),
    path('delete/<int:postagem_id>/', views.delete_postagem, name='delete'),
 """
 ]