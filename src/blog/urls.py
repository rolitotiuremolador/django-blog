from django.urls import path, re_path
from blog.views import (
    blog_post_detail_view, 
    blog_post_list_view, 
    blog_post_delete_view,
    blog_post_update_view,
    )

urlpatterns = [
    path('', blog_post_list_view),
    path('<str:slug>/', blog_post_detail_view),
    path('<str:slug>/delete/', blog_post_delete_view),
    path('<str:slug>/update/', blog_post_update_view),
]
