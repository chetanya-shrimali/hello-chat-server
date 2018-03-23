from django.conf.urls import url
from django.urls import path
from chat_app import views


app_name = 'chat_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]