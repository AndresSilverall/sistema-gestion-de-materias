from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home" ),
    path('register/', views.register_topic, name="register" ),
    path('update/', views.update_topic, name="update" ),
    path('delete/<pk>', views.delete_topic, name="delete" ),
    path('info/', views.info_user, name="info" ),
    path('search/', views.search_topic, name="search" )
]
