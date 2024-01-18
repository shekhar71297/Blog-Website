from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view.as_view()),
    path('images',views.imageview.as_view()),

] 
