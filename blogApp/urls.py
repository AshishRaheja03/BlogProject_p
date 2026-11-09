from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogsListView, name='home'),
    path("<int:blog_pk>/", views.blogDetailView, name='blog_detail'),
    path("dashboard/<str:username>/", views.userDashboardView, name='dashboard'),
    path("submitblog/", views.submitBlogView, name='submit_blog'),
]