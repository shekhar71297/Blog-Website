from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomePage, name='home'),
    path('about/', views.AboutPage, name='about'),
    path('post/<slug:slug>', views.PostPage, name='post'),
    path('posts/<slug:slug>',views.PostDetails,name='posts')
]
