from django.urls import path

from . import views

urlpatterns = [
  path('', views.forum_view, name='forum'),
  path('<int:pk>/', views.forum_topics, name='forum_topics'),
  path('<int:pk>/new/', views.new_topic, name='new_topic'),
]