from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
]