from django.urls import path
from user_profile import views

app_name = "profile"
urlpatterns = [
    path('', views.profile, name = 'profile')
]
