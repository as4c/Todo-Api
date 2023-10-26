from django.urls import path
from . import views

urlpatterns = [
    path('create-todo/', views.TaskCreateAPIView.as_view(), name='create-todo'),
    path('todos/', views.TaskAPIView.as_view(), name='todo-list'),
    path('todo/<int:pk>/', views.TaskDetailAPIView.as_view(), name='todos'),
    path('create-tag/',views.TagCreateAPIView.as_view(),name="create-tag"),
    path("tags/",views.TagAPIView.as_view(),name='tags'),
    path('tags/<int:pk>/',views.TagDetailAPIView.as_view(),name='detail-tags'),
    path('', views.homepage, name = 'home'),
     path('thumbnail/', views.create_thumbnail, name = 'thumbnail'),
]
