from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('post', views.blog_post),
    path('post/<slug>', views.PostDetail.as_view()),
    path('post/like/<slug>', views.like),
    path('post/unlike/<slug>', views.unlike)
]
