from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',
         views.index,
         name ='landing-index'),
    path('servicos/<str:path>',
         views.servicos,
         name ='landing-servicos'),
     path('blog',
         views.blog,
         name ='landing-blog'),
     path('blogPost/<int:id>',
         views.blogPost,
         name ='landing-blogPost'),
    path('vue-test', views.vue_test),
  

]


