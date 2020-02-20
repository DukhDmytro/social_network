from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('post', views.BlogPost.as_view()),
    path('post/<slug>', views.PostDetail.as_view()),
    path('post/like/<slug>', views.Like.as_view()),
    path('post/unlike/<slug>', views.Unlike.as_view())
]
