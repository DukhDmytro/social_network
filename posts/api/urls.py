from django.urls import path
from .views import create_post, post_details, like, unlike

app_name = 'posts'

urlpatterns = [
    path('post', create_post),
    path('post/<slug>', post_details),
    path('post/like/<slug>', like),
    path('post/unlike/<slug>', unlike)
]
