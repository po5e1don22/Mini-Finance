from django.urls import path
from transactions import views

app_name = 'wallet'
urlpatterns = [
    path('', views.wallet, name = 'wallet'),
    path ('info/', views.transation_detail, name = 'transation_detail'),
    path ('transfer/', views.transfer, name = 'transfer' )
]
