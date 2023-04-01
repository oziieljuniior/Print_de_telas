from django.urls import path
from .views import DashboardView, ProfileView

app_name = 'atconnect'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]
