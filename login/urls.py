from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.form_login, name="login" )
   
]
