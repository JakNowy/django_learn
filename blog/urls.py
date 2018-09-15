from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    # przyjmij argument pk i uzyj jej w URLu
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.AboutView.as_view(), name='blog-about'),
]