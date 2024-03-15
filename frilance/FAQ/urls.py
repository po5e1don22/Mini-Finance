from django.urls import path
from FAQ import views

app_name = "FAQ"
urlpatterns = [
    path('', views.FAQ, name = "FAQ")
]
