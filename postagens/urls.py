from django.urls import path

from . import views

app_name = 'postagens'
urlpatterns = [
    path("", views.PostagemListView.as_view(), name="index"),
    path("search/", views.search_postagens, name="search"),
    path('create/', views.PostagemCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostagemDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.PostagemUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostagemDeleteView.as_view(), name='delete'),
    path('<int:postagem_id>/review/', views.create_review, name='review'),
    path('lists/', views.ListListView.as_view(), name='lists'),
    path('lists/create', views.ListCreateView.as_view(), name='create-list'),
 ]