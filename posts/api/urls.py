from django.urls import path
from .views import create_post, post_details

app_name = 'posts'

urlpatterns = [
    path('post', create_post),
    path('post/<slug>', post_details)
]
