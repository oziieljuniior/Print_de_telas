from django.urls import path
from .views import DashboardView, ProfileView, ProfileSearchVIew, MyModelView

app_name = 'atconnect'

urlpatterns = [
    path('profile/<int:pk>/', ProfileView, name='profile'),
    path('profile/search/', ProfileSearchVIew.as_view(), name = 'profile_search'),
    path('', DashboardView.as_view(), name ='dashboard'),
    path('my-url/', MyModelView.as_view(), name="my-url"),
]
