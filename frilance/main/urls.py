from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name = 'main'),
    path ('login/', views.login_views, name = 'login' ),
    path('logout/', views.logout_views, name = 'logout'),
    path('registration/', views.register_views, name = 'registration')
]
