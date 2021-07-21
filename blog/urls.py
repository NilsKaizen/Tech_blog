from django.urls import path
from . import views

app_name="blog"

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/create_post', views.create_post, name="create_post"),
    path('blog/post/<int:post_pk>', views.view_post, name="view_post"),
    path('blog/draft_posts', views.draft_posts, name="draft_posts"),
    # path('blog/delete_post', views.delete_post, name="delete_post"),
]
