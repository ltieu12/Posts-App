from django.urls import path
from . import views

app = "posts"

urlpatterns = [
    path("", views.posts_list)
]
