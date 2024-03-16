from django.urls import path
from user_profile import views

app_name = "profile"
urlpatterns = [
    path('profile/', views.profile, name = 'profile')
]
