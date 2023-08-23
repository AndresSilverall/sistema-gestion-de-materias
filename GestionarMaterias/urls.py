from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home" ),
    path('register/', views.register_topic, name="register" ),
    path('info/', views.info_user, name="info" ),
    path('login/', views.form_login, name="login" )
]
