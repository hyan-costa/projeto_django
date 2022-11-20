from django.urls import path
from . import views
urlpatterns = [
    path('create_user', views.create_user, name='create_user'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout_view'),
]