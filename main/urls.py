
from . import views
from django.urls import path

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('jackpot', views.jackpot, name='jackpot'),
    path('register', views.register, name='register'),
    path('lookup', views.lookup, name='lookup'),
] 