from django.urls import path
from .views import DashboardView, ProfileView, ProfileSearchVIew

app_name = 'atconnect'

urlpatterns = [
    path('profile/<int:pk>/', ProfileView, name='profile'),
    path('profile/search/', ProfileSearchVIew.as_view(), name = 'profile_search'),
]
