from django.urls import path
from settings import views

app_name = "settings"

urlpatterns = [
    path("", views.settings, name = 'settings'),
    path('settings/profile_update/', views.profile_update, name='profile_update'),
    path('settings/change_password/', views.change_password, name='change_password'),

]
