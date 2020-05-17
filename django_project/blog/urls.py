from django.urls import path
from . import views

#when /blog encountered in URL, website routes an empty string to the blog.urls.py file
#looks for which url pattern matches empty route (''). Then routed to views.home

#when /blog/about encountered in URL, "blog" is rerouted to this file.
urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about')

]