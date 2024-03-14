from django.urls import path
from .import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.index),
    path('<int:id>', views.post, name='post_detail'),
    path('register/', views.register, name='register'),
    path('', auth_view.LoginView.as_view(template_name='templates/login.html'), name='login'),
]