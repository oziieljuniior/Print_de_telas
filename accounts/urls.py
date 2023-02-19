from django.urls import path
from .views import DashboardView, ProfileListView, ProfileView, MyModelView, HomePageView, settings
from django.conf.urls import include

app_name = "System_Post"

urlpatterns = [
    path("", DashboardView.as_view() , name="dashboard"),
    path("settings/", settings, name = "settings"),
    path("profile/", ProfileListView.as_view(), name="profile_list"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("my-url/", MyModelView.as_view(), name = "my_url"),
]